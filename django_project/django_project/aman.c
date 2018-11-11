    #include<cv.h>
    #include<highgui.h>
   
   
		//To draw a histogram

	   IplImage* DrawHistogram(CvHistogram *hist, float scaleX=4, float scaleY=3)

	{
		float histMax = 0;
		cvGetMinMaxHistValue(hist, 0, &histMax, 0, 0);
		IplImage* imgHist = cvCreateImage(cvSize(256*scaleX, 64*scaleY), 8 ,1);
		cvZero(imgHist);

		for(int i=0;i<255;i++)
		
                      {
			float histValue = cvQueryHistValue_1D(hist, i);
			float nextValue = cvQueryHistValue_1D(hist, i+1);

			CvPoint pt1 = cvPoint(i*scaleX, 64*scaleY);
			CvPoint pt2 = cvPoint(i*scaleX+scaleX, 64*scaleY);
			CvPoint pt3 = cvPoint(i*scaleX+scaleX, (64-   nextValue*64/histMax)*scaleY);
			CvPoint pt4 = cvPoint(i*scaleX, (64-histValue*64/histMax)*scaleY);

			int numPts = 5;
			CvPoint pts[] = {pt1, pt2, pt3, pt4, pt1};

			cvFillConvexPoly(imgHist, pts, numPts, cvScalar(255));
		 }

		//Return histogram image
		return imgHist;
	}
		
                   //The main function

    int main(int argc, char *argv[])
    {
		//to track position of number plate in original image

		int xxx,yyy,www,hhh;
		long double decrement=100;

		{
			//IplImage is an image in OpenCV

			IplImage *img, *cc_color; 
			CvMemStorage *mem;
			img = cvLoadImage("C:/pictures/sample.jpg", 0);			
			
                       if( img == 0 ) 
			
                               {
				fprintf( stderr, "Cannot load file %s!\n", argv[1] );
				return 1; 
			}
			
		while(img->width>400||img->height>500)
		
                      	{
				IplImage *destination = cvCreateImage( cvSize((int)((img->width*95)/100) , (int)((img->height*95)/100) ) , img->depth , img->nChannels );
				cvResize(img, destination);
				img=cvCloneImage(destination);
				decrement=(decrement*95)/100;
			}
		
           	cc_color=cvCloneImage(img);
			
			{
				float max_value = 0.0;
				float min_value = 0.0;

	
                    			const char* name = "Histogram Equalization";
				IplImage* img_histeq = cvCreateImage( cvGetSize(img), IPL_DEPTH_8U, 1 );


				// Perform histogram equalization
                                         cvEqualizeHist( img, img_histeq );

				int numBins = 256;
				float range[] = {0, 255};
				float *ranges[] = { range };

				CvHistogram *hist = cvCreateHist(1, &numBins, CV_HIST_ARRAY, ranges, 1);
				cvClearHist(hist);


				cvCalcHist(&img_histeq, hist, 0, 0);

				IplImage* imgHistGrey = DrawHistogram(hist);					                    cvClearHist(hist);

				// Find the minimum and maximum values of the histograms 
				cvGetMinMaxHistValue( hist, &min_value , &max_value, 0, 0 ); 


				CvMat Ma;
				cvInitMatHeader(&Ma, 1, 4, CV_32S, img_histeq);

				CvScalar avg = cvAvg(&Ma);
				
				//Calculate average value
				double value = avg.val[0];
				
				cvAdaptiveThreshold(img, img, value, CV_ADAPTIVE_THRESH_GAUSSIAN_C, CV_THRESH_BINARY_INV, 5, 10) ;


			}
			
			IplImage* img_dilate = cvCloneImage(img);

			//Perform dilation for edge detection which is dilated image-binary image
			cvDilate(img,img_dilate,NULL,1);
			
	//Create an image to store edge detected result
			IplImage *img_sub = cvCreateImage(cvGetSize(img), img->depth, img->nChannels);
			cvZero(img_sub);
	        
			// load template image to track number plate
			IplImage *tpl = cvLoadImage("C:/pictures/rectangle.jpg",0);
			
			//Perform edge detection
			cvSub(  img_dilate , img , img_sub, NULL);
	 			
			IplImage *imgResult = cvCreateImage(cvSize(img_sub->width - tpl->width + 1 , img_sub->height - tpl->height + 1), IPL_DEPTH_32F, 1);
			
                               cvZero(imgResult);
		
			//Perform template matching to detect image
			cvMatchTemplate(img_sub, tpl, imgResult, CV_TM_SQDIFF);

			CvPoint    minloc, maxloc;
			double    minval, maxval;
			
			//Perform minmax function to locate the number plate detected in the image
			cvMinMaxLoc( imgResult, &minval, &maxval, &minloc, &maxloc, 0 );

			//Draw rectangle around the detected number plate
			cvRectangle(cc_color, cvPoint(minloc.x, minloc.y), cvPoint(minloc.x + tpl->width, minloc.y + tpl->height), CV_RGB(255, 0, 0), 1, 0, 0 );
			
			//Show detected number plate
			cvShowImage("numberplate",cc_color);
			
			cvWaitKey(0);
			
                           //Locate number plate in original image
			xxx=(int)((100/(decrement-3))*minloc.x);
			yyy=(int)((100/(decrement-2))*minloc.y);
			www=(int)((100/(decrement-1))*(minloc.x+tpl->width)-xxx);
			hhh=(int)((100/(decrement-1))*(minloc.y+tpl->height)-yyy);

			//Release image
		        cvReleaseImage( &img );
		
                    }

	IplImage *img, *cc_color; /*IplImage is an image in OpenCV*/
        CvMemStorage *mem;
        CvSeq *contours, *ptr;
       
		//Load original image
        img = cvLoadImage("C:/pictures/sample.jpg", 0);
		
                         if( img == 0 ) 
		
                      	{
				fprintf( stderr, "Cannot load file %s!\n", argv[1] );
				return 1; 
			}

		//Set number plate region as the region of interest
		cvSetImageROI(img, cvRect(xxx,yyy,www,hhh));
		
		cvShowImage("numberplate",img);
		
		cvWaitKey(0);

        {
            int height,width,step,channels;
            uchar *data;
            int i,j,k;




            // get the image data
            height    = img->height;
            width     = img->width;
            step      = img->widthStep;
            channels  = img->nChannels;
            data      = (uchar *)img->imageData;
            printf("Processing a %dx%d image with %d channels\n",height,width,channels);

            
            // invert the image
            for(i=0;i<height;i++) for(j=0;j<width;j++) for(k=0;k<channels;k++)
                data[i*step+j*channels+k]=255-data[i*step+j*channels+k];

            // show the image
            //cvShowImage("image", img );
            //cvWaitKey(0);
        }
		
        IplImage* tempImg;
        tempImg=cvCloneImage(img);

		
 //Pre Processing on the number plate
 
       cvMorphologyEx(img,img,tempImg,CV_SHAPE_RECT,CV_MEDIAN,1);
        cvReleaseImage( &tempImg );
        cc_color = cvCreateImage(cvGetSize(img), IPL_DEPTH_8U, 3);
        cvThreshold(img, img, 150, 255, CV_THRESH_OTSU);
        cvMorphologyEx(img,img,tempImg,CV_SHAPE_RECT,CV_MOP_ERODE,1);
        cvMorphologyEx(img,img,tempImg,CV_SHAPE_RECT,CV_MOP_CLOSE,1);
        cvMorphologyEx(img,img,tempImg,CV_SHAPE_RECT,CV_MOP_OPEN,1);
        cvMorphologyEx(img,img,tempImg,CV_SHAPE_RECT,CV_MOP_DILATE,1);
        cvMorphologyEx(img,img,tempImg,CV_SHAPE_RECT,CV_MEDIAN,1);
        
        
        mem = cvCreateMemStorage(0);
       



		//Check total number of contour in the image
        int t=cvFindContours(img, mem, &contours, sizeof(CvContour), CV_RETR_CCOMP,
            CV_CHAIN_APPROX_SIMPLE, cvPoint(0,0));
       


//Assume maximum contour founded are less than 100, create an iplimage array to store these contours

        IplImage *frame_buffer[100];
        IplImage *frame_buffer1[100];

        int count=0;
        char buff[1000];

//track position of the charater in the image
 int distancefromleft[100];

		//to store sorten position of characters
        int numberpositions[100];
        int x=0;
        for (int i = 0; i < 100; i++)
        {
            numberpositions[i]=-1;
        }

        for (ptr = contours; ptr != NULL; ptr = ptr->h_next)
        {
            frame_buffer[count]=cvCreateImage( cvGetSize(cc_color), cc_color->depth, 1 );           
            cvZero(frame_buffer[count]);
            CvScalar color = CV_RGB( 255, 255, 255 );
			
//Draw bounding box on the contour
            CvRect boundbox = cvBoundingRect(ptr);
			
//Draw rectangle on the contour   cvRectangle(frame_buffer[count],cvPoint(boundbox.x,boundbox.y),cvPoint((boundbox.x+boundbox.width),(boundbox.y+boundbox.height)),CV_RGB(255,0,0),1,8,0);
          

 //copy contours to image array
			cvDrawContours(frame_buffer[count], ptr, color, CV_RGB(0,0,0), -1, CV_FILLED, 8, cvPoint(0,0));

 //Check if contour can be a character or noise           
            if((boundbox.width*boundbox.height)>500&&boundbox.width<100&&boundbox.height<100&&boundbox.width>10&&boundbox.height>45)
			{
				//Store

				frame_buffer1[x]=cvCreateImage(cvSize(boundbox.width-1,boundbox.height-1), cc_color->depth, 1 );
				frame_buffer1[x]->origin=frame_buffer[count]->origin;
				frame_buffer1[x]->widthStep=frame_buffer[count]->widthStep;


				frame_buffer1[x]->imageData=frame_buffer[count]->imageData+(boundbox.y+1)*frame_buffer[count]->widthStep+(boundbox.x+1)*frame_buffer[count]->nChannels;
				sprintf( buff, "%d", count );

				//Store distance from left of the character
				distancefromleft[x]=boundbox.x;
				printf("contour no. = %d \t distance from left = %d \n",x,distancefromleft[x]);

				//Sort the character positions
				numberpositions[x]=x;
				sprintf( buff, "%s.jpg", buff );

				//Save the contour in the current folder
				cvSaveImage( buff, frame_buffer1[x] );
				sprintf( buff, "" );
				x++;
            }
            count++;
        }
                   

        int temp,temp1;

       //Sort the positions of the characters in the number plate
        for (int i = 0; i < x; i++)
        {
            temp=distancefromleft[i];
            temp1=numberpositions[i];
           
            for (int j = i; j < x; j++)
            {
                if (distancefromleft[j] < temp)
                {
                    distancefromleft[i]=distancefromleft[j];
                    distancefromleft[j]=temp;
                    temp=distancefromleft[i];

                    numberpositions[i]=numberpositions[j];
                    numberpositions[j]=temp1;

                    temp1=numberpositions[i];            
                }
            }
		}
      

		//Loading the templates

        IplImage *templates[10];
		templates[0]=cvLoadImage("C:/pictures/0.jpg", 0);
		templates[1]=cvLoadImage("C:/pictures/1.jpg", 0);
		templates[2]=cvLoadImage("C:/pictures/2.jpg", 0);
		templates[3]=cvLoadImage("C:/pictures/3.jpg", 0);
		templates[4]=cvLoadImage("C:/pictures/4.jpg", 0);
		templates[5]=cvLoadImage("C:/pictures/5.jpg", 0);
		templates[6]=cvLoadImage("C:/pictures/6.jpg", 0);
		templates[7]=cvLoadImage("C:/pictures/7.jpg", 0);
		templates[8]=cvLoadImage("C:/pictures/8.jpg", 0);
		templates[9]=cvLoadImage("C:/pictures/9.jpg", 0);
        

        char templatename[10]={'7','A','H','0','1','6','5','M','2','V'};
        char result[20];
       
        for (int i = 0; i < x; i++)
        {
			result[i]='_';
        }
       
        for (int i = 0; i < x; i++)
        {
           for(int j = 0;j < 10; j++)
		   { 
			   //Check if the template is valid for cvmatchtemplate function
			   if(((templates[j]->width)>(frame_buffer1[numberpositions[i]]->width))|| ((templates[j]->height)>(frame_buffer1[numberpositions[i]]->height)))
       
               {
                    continue;
                }
			   


                //Make iplimage for cvmatchtemplate function result
				IplImage* imgResult = cvCreateImage(cvSize(frame_buffer1[numberpositions[i]]->width - templates[j]->width + 1 , frame_buffer1[numberpositions[i]]->height - templates[j]->height + 1), IPL_DEPTH_32F, 1);
                cvZero(imgResult);

				cvMatchTemplate(frame_buffer1[numberpositions[i]], templates[j],imgResult, CV_TM_SQDIFF);   
               
				double min_val=0, max_val=0,maxx=0, minn=0;
               
                CvPoint min_loc, max_loc;
                cvMinMaxLoc(imgResult, &min_val, &max_val, &min_loc, &max_loc);
                
                cvReleaseImage( &imgResult );
                               
            
                                         char temp11[20], temp12[20];
				sprintf( temp11, "%d", max_val );
				sprintf( temp12, "%d", min_val );

				//Check if the result is 0, if not, check for the next template
				if(temp11[0]!='0')
				{
					continue;
				}
				if(temp12[0]!='0')
				{
					continue;
				}
				result[i]=templatename[j];
				printf("number added to the result = %c \n", templatename[j]);
				break;
           
		   }	
        }
        
		//Print the result
		for(int i=0;i<10;i++)
        {

            printf("%c",result[i]);
        }
        cvWaitKey(0);       

        /* free memory */
        cvDestroyWindow( "image" );
        cvReleaseImage( &img );
        cvReleaseImage(&cc_color);

    return 0;
    }
