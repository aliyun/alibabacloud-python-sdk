# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeDeviceServiceResponseBody(DaraModel):
    def __init__(
        self,
        app_meta_data: main_models.DescribeDeviceServiceResponseBodyAppMetaData = None,
        app_status: main_models.DescribeDeviceServiceResponseBodyAppStatus = None,
        request_id: str = None,
        resource_detail_infos: List[main_models.DescribeDeviceServiceResponseBodyResourceDetailInfos] = None,
        resource_infos: List[main_models.DescribeDeviceServiceResponseBodyResourceInfos] = None,
    ):
        # The basic properties of the application.
        self.app_meta_data = app_meta_data
        # The status information of the application.
        self.app_status = app_status
        # The ID of the request.
        self.request_id = request_id
        # The information about the devices.
        self.resource_detail_infos = resource_detail_infos
        # The information about the instances.
        self.resource_infos = resource_infos

    def validate(self):
        if self.app_meta_data:
            self.app_meta_data.validate()
        if self.app_status:
            self.app_status.validate()
        if self.resource_detail_infos:
            for v1 in self.resource_detail_infos:
                 if v1:
                    v1.validate()
        if self.resource_infos:
            for v1 in self.resource_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_meta_data is not None:
            result['AppMetaData'] = self.app_meta_data.to_map()

        if self.app_status is not None:
            result['AppStatus'] = self.app_status.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceDetailInfos'] = []
        if self.resource_detail_infos is not None:
            for k1 in self.resource_detail_infos:
                result['ResourceDetailInfos'].append(k1.to_map() if k1 else None)

        result['ResourceInfos'] = []
        if self.resource_infos is not None:
            for k1 in self.resource_infos:
                result['ResourceInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppMetaData') is not None:
            temp_model = main_models.DescribeDeviceServiceResponseBodyAppMetaData()
            self.app_meta_data = temp_model.from_map(m.get('AppMetaData'))

        if m.get('AppStatus') is not None:
            temp_model = main_models.DescribeDeviceServiceResponseBodyAppStatus()
            self.app_status = temp_model.from_map(m.get('AppStatus'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_detail_infos = []
        if m.get('ResourceDetailInfos') is not None:
            for k1 in m.get('ResourceDetailInfos'):
                temp_model = main_models.DescribeDeviceServiceResponseBodyResourceDetailInfos()
                self.resource_detail_infos.append(temp_model.from_map(k1))

        self.resource_infos = []
        if m.get('ResourceInfos') is not None:
            for k1 in m.get('ResourceInfos'):
                temp_model = main_models.DescribeDeviceServiceResponseBodyResourceInfos()
                self.resource_infos.append(temp_model.from_map(k1))

        return self

class DescribeDeviceServiceResponseBodyResourceInfos(DaraModel):
    def __init__(
        self,
        app_version: str = None,
        area_code: str = None,
        area_name: str = None,
        create_time: str = None,
        device_infos: List[main_models.DescribeDeviceServiceResponseBodyResourceInfosDeviceInfos] = None,
        instance_id: str = None,
        instance_status: str = None,
        internal_ips: List[main_models.DescribeDeviceServiceResponseBodyResourceInfosInternalIps] = None,
        public_ips: List[main_models.DescribeDeviceServiceResponseBodyResourceInfosPublicIps] = None,
        region_code: str = None,
        region_id: str = None,
        region_name: str = None,
    ):
        # The version of the application.
        self.app_version = app_version
        # The area code.
        self.area_code = area_code
        # The region name.
        self.area_name = area_name
        # The time when the application was created.
        self.create_time = create_time
        # The information about the devices.
        self.device_infos = device_infos
        # The ID of the instance.
        self.instance_id = instance_id
        # The status of the instance.
        self.instance_status = instance_status
        # The internal IP addresses.
        self.internal_ips = internal_ips
        # The public IP addresses.
        self.public_ips = public_ips
        # The ID of the region.
        self.region_code = region_code
        # The ID of the ENS node.
        self.region_id = region_id
        # The name of the region.
        self.region_name = region_name

    def validate(self):
        if self.device_infos:
            for v1 in self.device_infos:
                 if v1:
                    v1.validate()
        if self.internal_ips:
            for v1 in self.internal_ips:
                 if v1:
                    v1.validate()
        if self.public_ips:
            for v1 in self.public_ips:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.area_code is not None:
            result['AreaCode'] = self.area_code

        if self.area_name is not None:
            result['AreaName'] = self.area_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        result['DeviceInfos'] = []
        if self.device_infos is not None:
            for k1 in self.device_infos:
                result['DeviceInfos'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        result['InternalIps'] = []
        if self.internal_ips is not None:
            for k1 in self.internal_ips:
                result['InternalIps'].append(k1.to_map() if k1 else None)

        result['PublicIps'] = []
        if self.public_ips is not None:
            for k1 in self.public_ips:
                result['PublicIps'].append(k1.to_map() if k1 else None)

        if self.region_code is not None:
            result['RegionCode'] = self.region_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.region_name is not None:
            result['RegionName'] = self.region_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('AreaCode') is not None:
            self.area_code = m.get('AreaCode')

        if m.get('AreaName') is not None:
            self.area_name = m.get('AreaName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        self.device_infos = []
        if m.get('DeviceInfos') is not None:
            for k1 in m.get('DeviceInfos'):
                temp_model = main_models.DescribeDeviceServiceResponseBodyResourceInfosDeviceInfos()
                self.device_infos.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        self.internal_ips = []
        if m.get('InternalIps') is not None:
            for k1 in m.get('InternalIps'):
                temp_model = main_models.DescribeDeviceServiceResponseBodyResourceInfosInternalIps()
                self.internal_ips.append(temp_model.from_map(k1))

        self.public_ips = []
        if m.get('PublicIps') is not None:
            for k1 in m.get('PublicIps'):
                temp_model = main_models.DescribeDeviceServiceResponseBodyResourceInfosPublicIps()
                self.public_ips.append(temp_model.from_map(k1))

        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        return self

class DescribeDeviceServiceResponseBodyResourceInfosPublicIps(DaraModel):
    def __init__(
        self,
        ip: str = None,
    ):
        # The public IP address.
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['Ip'] = self.ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        return self

class DescribeDeviceServiceResponseBodyResourceInfosInternalIps(DaraModel):
    def __init__(
        self,
        ip: str = None,
    ):
        # The internal IP address.
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['Ip'] = self.ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        return self

class DescribeDeviceServiceResponseBodyResourceInfosDeviceInfos(DaraModel):
    def __init__(
        self,
        name: str = None,
        network: List[main_models.DescribeDeviceServiceResponseBodyResourceInfosDeviceInfosNetwork] = None,
        status: str = None,
    ):
        # The name of the device.
        self.name = name
        # The network information.
        self.network = network
        # The status.
        self.status = status

    def validate(self):
        if self.network:
            for v1 in self.network:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        result['Network'] = []
        if self.network is not None:
            for k1 in self.network:
                result['Network'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.network = []
        if m.get('Network') is not None:
            for k1 in m.get('Network'):
                temp_model = main_models.DescribeDeviceServiceResponseBodyResourceInfosDeviceInfosNetwork()
                self.network.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeDeviceServiceResponseBodyResourceInfosDeviceInfosNetwork(DaraModel):
    def __init__(
        self,
        container_ports: str = None,
        external_ip: str = None,
        host_ports: str = None,
        protocol: str = None,
    ):
        # The port of the container.
        self.container_ports = container_ports
        # The public IP address.
        self.external_ip = external_ip
        # The port range.
        self.host_ports = host_ports
        # The protocol of the gateway. The value is of the enumeration type. Valid values:
        # 
        # *   TCP
        # *   UDP
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_ports is not None:
            result['ContainerPorts'] = self.container_ports

        if self.external_ip is not None:
            result['ExternalIp'] = self.external_ip

        if self.host_ports is not None:
            result['HostPorts'] = self.host_ports

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerPorts') is not None:
            self.container_ports = m.get('ContainerPorts')

        if m.get('ExternalIp') is not None:
            self.external_ip = m.get('ExternalIp')

        if m.get('HostPorts') is not None:
            self.host_ports = m.get('HostPorts')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

class DescribeDeviceServiceResponseBodyResourceDetailInfos(DaraModel):
    def __init__(
        self,
        device_name: str = None,
        id: str = None,
        ip: str = None,
        isp: str = None,
        image_id: str = None,
        mac: str = None,
        region_id: str = None,
        server: str = None,
        status: str = None,
        type: str = None,
    ):
        # The name of the device.
        self.device_name = device_name
        # The ID of the cloud device.
        self.id = id
        # The IP address.
        self.ip = ip
        # The Internet service provider (ISP).
        self.isp = isp
        # The ID of the image.
        self.image_id = image_id
        # The media access control (MAC) address of the device.
        self.mac = mac
        # The ID of the ENS node.
        self.region_id = region_id
        # The server name of the ENS node.
        self.server = server
        # The status of the device.
        self.status = status
        # The type of the device.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.id is not None:
            result['ID'] = self.id

        if self.ip is not None:
            result['IP'] = self.ip

        if self.isp is not None:
            result['ISP'] = self.isp

        if self.image_id is not None:
            result['ImageID'] = self.image_id

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.region_id is not None:
            result['RegionID'] = self.region_id

        if self.server is not None:
            result['Server'] = self.server

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('ID') is not None:
            self.id = m.get('ID')

        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('ISP') is not None:
            self.isp = m.get('ISP')

        if m.get('ImageID') is not None:
            self.image_id = m.get('ImageID')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('RegionID') is not None:
            self.region_id = m.get('RegionID')

        if m.get('Server') is not None:
            self.server = m.get('Server')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeDeviceServiceResponseBodyAppStatus(DaraModel):
    def __init__(
        self,
        phase: str = None,
        status_descrip: str = None,
        update_time: str = None,
    ):
        # The status of the application. The value is of the enumeration type. Valid values:
        # 
        # Three intermediate states:
        # 
        # *   CREATING
        # *   UPDATING
        # *   DELETING
        # 
        # Four final states:
        # 
        # *   CREATE_FAILED
        # *   UPDATE_FAILED
        # *   DELETE_FAILED
        # *   RUNNING
        self.phase = phase
        # The description of the application status.
        self.status_descrip = status_descrip
        # The time when the status was last updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.phase is not None:
            result['Phase'] = self.phase

        if self.status_descrip is not None:
            result['StatusDescrip'] = self.status_descrip

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('StatusDescrip') is not None:
            self.status_descrip = m.get('StatusDescrip')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class DescribeDeviceServiceResponseBodyAppMetaData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_stable_version: str = None,
        app_type: str = None,
        cluster_name: str = None,
        create_time: str = None,
        description: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name
        # The stable version number of the application.
        self.app_stable_version = app_stable_version
        # The type of the application. The value is of the enumeration type. Valid values:
        # 
        # *   Common
        # *   Scheduler
        self.app_type = app_type
        # The name of the application cluster.
        self.cluster_name = cluster_name
        # The time when the application was created.
        self.create_time = create_time
        # The description of the application.
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_stable_version is not None:
            result['AppStableVersion'] = self.app_stable_version

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppStableVersion') is not None:
            self.app_stable_version = m.get('AppStableVersion')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        return self

