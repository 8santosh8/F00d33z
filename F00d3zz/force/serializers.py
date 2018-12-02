from rest_framework import serializers
from force.models import EquationLog,UserLog

class UserLogSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserLog
        fields=('fullname','email')

class EquationLogSerializer(serializers.ModelSerializer):
    userlogid=UserLogSerializer()
    class Meta:
        model=EquationLog
        fields=('mass1','position1','mass2','position2','com','userlogid')
        read_only_fields=('com',)

    def create(self, validated_data):
        userlogid_data=validated_data.pop('userlogid')
        userlogid=UserLog.objects.create(**userlogid_data)
        mass1=validated_data['mass1']
        position1=validated_data['position1']
        mass2=validated_data['mass2']
        position2=validated_data['position2']
        com = ((float(mass1) * float(position1)) + (float(mass2) * float(position2))) / (float(position1) + float(position2))
        equationlog=EquationLog.objects.create(com=com, userlogid=userlogid, **validated_data)
        return equationlog