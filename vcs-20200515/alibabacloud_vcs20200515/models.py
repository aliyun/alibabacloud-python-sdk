# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class AddAiotDevicesRequestAiotDeviceList(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        device_id: str = None,
        name: str = None,
        ipaddr: str = None,
        port: int = None,
        longitude: float = None,
        latitude: float = None,
        place: str = None,
    ):
        self.corp_id = corp_id
        self.device_id = device_id
        self.name = name
        self.ipaddr = ipaddr
        self.port = port
        self.longitude = longitude
        self.latitude = latitude
        self.place = place

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.name is not None:
            result['Name'] = self.name
        if self.ipaddr is not None:
            result['IPAddr'] = self.ipaddr
        if self.port is not None:
            result['Port'] = self.port
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.place is not None:
            result['Place'] = self.place
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('IPAddr') is not None:
            self.ipaddr = m.get('IPAddr')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Place') is not None:
            self.place = m.get('Place')
        return self


class AddAiotDevicesRequest(TeaModel):
    def __init__(
        self,
        aiot_device_list: List[AddAiotDevicesRequestAiotDeviceList] = None,
    ):
        self.aiot_device_list = aiot_device_list

    def validate(self):
        if self.aiot_device_list:
            for k in self.aiot_device_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AiotDeviceList'] = []
        if self.aiot_device_list is not None:
            for k in self.aiot_device_list:
                result['AiotDeviceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aiot_device_list = []
        if m.get('AiotDeviceList') is not None:
            for k in m.get('AiotDeviceList'):
                temp_model = AddAiotDevicesRequestAiotDeviceList()
                self.aiot_device_list.append(temp_model.from_map(k))
        return self


class AddAiotDevicesShrinkRequest(TeaModel):
    def __init__(
        self,
        aiot_device_list_shrink: str = None,
    ):
        self.aiot_device_list_shrink = aiot_device_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aiot_device_list_shrink is not None:
            result['AiotDeviceList'] = self.aiot_device_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiotDeviceList') is not None:
            self.aiot_device_list_shrink = m.get('AiotDeviceList')
        return self


class AddAiotDevicesResponseBodyResultList(TeaModel):
    def __init__(
        self,
        id: str = None,
        server_id: str = None,
        server_ip: str = None,
        server_host: str = None,
        server_port: str = None,
        server_wss_port: str = None,
        device_id: str = None,
        user_id: str = None,
        password: str = None,
        code: str = None,
        message: str = None,
    ):
        self.id = id
        self.server_id = server_id
        self.server_ip = server_ip
        self.server_host = server_host
        self.server_port = server_port
        self.server_wss_port = server_wss_port
        self.device_id = device_id
        self.user_id = user_id
        self.password = password
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.server_host is not None:
            result['ServerHost'] = self.server_host
        if self.server_port is not None:
            result['ServerPort'] = self.server_port
        if self.server_wss_port is not None:
            result['ServerWssPort'] = self.server_wss_port
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.password is not None:
            result['Password'] = self.password
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('ServerHost') is not None:
            self.server_host = m.get('ServerHost')
        if m.get('ServerPort') is not None:
            self.server_port = m.get('ServerPort')
        if m.get('ServerWssPort') is not None:
            self.server_wss_port = m.get('ServerWssPort')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AddAiotDevicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        result_list: List[AddAiotDevicesResponseBodyResultList] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message
        self.result_list = result_list

    def validate(self):
        if self.result_list:
            for k in self.result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['ResultList'] = []
        if self.result_list is not None:
            for k in self.result_list:
                result['ResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.result_list = []
        if m.get('ResultList') is not None:
            for k in m.get('ResultList'):
                temp_model = AddAiotDevicesResponseBodyResultList()
                self.result_list.append(temp_model.from_map(k))
        return self


class AddAiotDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddAiotDevicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddAiotDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddAiotPersonTableRequestPersonTable(TeaModel):
    def __init__(
        self,
        person_table_id: str = None,
        name: str = None,
        type: int = None,
        verification_model_list: List[int] = None,
    ):
        self.person_table_id = person_table_id
        self.name = name
        self.type = type
        self.verification_model_list = verification_model_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.person_table_id is not None:
            result['PersonTableId'] = self.person_table_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.verification_model_list is not None:
            result['VerificationModelList'] = self.verification_model_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PersonTableId') is not None:
            self.person_table_id = m.get('PersonTableId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VerificationModelList') is not None:
            self.verification_model_list = m.get('VerificationModelList')
        return self


class AddAiotPersonTableRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        person_table: AddAiotPersonTableRequestPersonTable = None,
    ):
        self.id = id
        self.person_table = person_table

    def validate(self):
        if self.person_table:
            self.person_table.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.person_table is not None:
            result['PersonTable'] = self.person_table.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PersonTable') is not None:
            temp_model = AddAiotPersonTableRequestPersonTable()
            self.person_table = temp_model.from_map(m['PersonTable'])
        return self


class AddAiotPersonTableResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        person_table_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message
        self.person_table_id = person_table_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.person_table_id is not None:
            result['PersonTableId'] = self.person_table_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PersonTableId') is not None:
            self.person_table_id = m.get('PersonTableId')
        return self


class AddAiotPersonTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddAiotPersonTableResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddAiotPersonTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddAiotPersonTableItemRequestPersonTableItemIdentificationList(TeaModel):
    def __init__(
        self,
        type: int = None,
        number: str = None,
    ):
        self.type = type
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.number is not None:
            result['Number'] = self.number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        return self


class AddAiotPersonTableItemRequestPersonTableItemImageListFeatureInfo(TeaModel):
    def __init__(
        self,
        vendor: str = None,
        algorithm_version: str = None,
        algorithm_type: str = None,
        tab_id: str = None,
        oject_id: str = None,
        image_id: str = None,
        feature_data: str = None,
    ):
        self.vendor = vendor
        self.algorithm_version = algorithm_version
        self.algorithm_type = algorithm_type
        self.tab_id = tab_id
        self.oject_id = oject_id
        self.image_id = image_id
        self.feature_data = feature_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.algorithm_version is not None:
            result['AlgorithmVersion'] = self.algorithm_version
        if self.algorithm_type is not None:
            result['AlgorithmType'] = self.algorithm_type
        if self.tab_id is not None:
            result['TabId'] = self.tab_id
        if self.oject_id is not None:
            result['OjectId'] = self.oject_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.feature_data is not None:
            result['FeatureData'] = self.feature_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('AlgorithmVersion') is not None:
            self.algorithm_version = m.get('AlgorithmVersion')
        if m.get('AlgorithmType') is not None:
            self.algorithm_type = m.get('AlgorithmType')
        if m.get('TabId') is not None:
            self.tab_id = m.get('TabId')
        if m.get('OjectId') is not None:
            self.oject_id = m.get('OjectId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('FeatureData') is not None:
            self.feature_data = m.get('FeatureData')
        return self


class AddAiotPersonTableItemRequestPersonTableItemImageList(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        event_sort: str = None,
        device_id: str = None,
        storage_path: str = None,
        size: int = None,
        type: str = None,
        file_format: str = None,
        shot_time: str = None,
        width: int = None,
        height: int = None,
        data: str = None,
        feature_info: AddAiotPersonTableItemRequestPersonTableItemImageListFeatureInfo = None,
    ):
        self.image_id = image_id
        self.event_sort = event_sort
        self.device_id = device_id
        self.storage_path = storage_path
        self.size = size
        self.type = type
        self.file_format = file_format
        self.shot_time = shot_time
        self.width = width
        self.height = height
        self.data = data
        self.feature_info = feature_info

    def validate(self):
        if self.feature_info:
            self.feature_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.event_sort is not None:
            result['EventSort'] = self.event_sort
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.storage_path is not None:
            result['StoragePath'] = self.storage_path
        if self.size is not None:
            result['Size'] = self.size
        if self.type is not None:
            result['Type'] = self.type
        if self.file_format is not None:
            result['FileFormat'] = self.file_format
        if self.shot_time is not None:
            result['ShotTime'] = self.shot_time
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.data is not None:
            result['Data'] = self.data
        if self.feature_info is not None:
            result['FeatureInfo'] = self.feature_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('EventSort') is not None:
            self.event_sort = m.get('EventSort')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('StoragePath') is not None:
            self.storage_path = m.get('StoragePath')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')
        if m.get('ShotTime') is not None:
            self.shot_time = m.get('ShotTime')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('FeatureInfo') is not None:
            temp_model = AddAiotPersonTableItemRequestPersonTableItemImageListFeatureInfo()
            self.feature_info = temp_model.from_map(m['FeatureInfo'])
        return self


class AddAiotPersonTableItemRequestPersonTableItem(TeaModel):
    def __init__(
        self,
        person_table_id: str = None,
        person_id: str = None,
        last_change: str = None,
        person_code: str = None,
        person_name: str = None,
        remarks: str = None,
        time_template_num: int = None,
        identification_num: int = None,
        identification_list: List[AddAiotPersonTableItemRequestPersonTableItemIdentificationList] = None,
        image_num: int = None,
        image_list: List[AddAiotPersonTableItemRequestPersonTableItemImageList] = None,
    ):
        self.person_table_id = person_table_id
        self.person_id = person_id
        self.last_change = last_change
        self.person_code = person_code
        self.person_name = person_name
        self.remarks = remarks
        self.time_template_num = time_template_num
        self.identification_num = identification_num
        self.identification_list = identification_list
        self.image_num = image_num
        self.image_list = image_list

    def validate(self):
        if self.identification_list:
            for k in self.identification_list:
                if k:
                    k.validate()
        if self.image_list:
            for k in self.image_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.person_table_id is not None:
            result['PersonTableId'] = self.person_table_id
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.last_change is not None:
            result['LastChange'] = self.last_change
        if self.person_code is not None:
            result['PersonCode'] = self.person_code
        if self.person_name is not None:
            result['PersonName'] = self.person_name
        if self.remarks is not None:
            result['Remarks'] = self.remarks
        if self.time_template_num is not None:
            result['TimeTemplateNum'] = self.time_template_num
        if self.identification_num is not None:
            result['IdentificationNum'] = self.identification_num
        result['IdentificationList'] = []
        if self.identification_list is not None:
            for k in self.identification_list:
                result['IdentificationList'].append(k.to_map() if k else None)
        if self.image_num is not None:
            result['ImageNum'] = self.image_num
        result['ImageList'] = []
        if self.image_list is not None:
            for k in self.image_list:
                result['ImageList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PersonTableId') is not None:
            self.person_table_id = m.get('PersonTableId')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('LastChange') is not None:
            self.last_change = m.get('LastChange')
        if m.get('PersonCode') is not None:
            self.person_code = m.get('PersonCode')
        if m.get('PersonName') is not None:
            self.person_name = m.get('PersonName')
        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')
        if m.get('TimeTemplateNum') is not None:
            self.time_template_num = m.get('TimeTemplateNum')
        if m.get('IdentificationNum') is not None:
            self.identification_num = m.get('IdentificationNum')
        self.identification_list = []
        if m.get('IdentificationList') is not None:
            for k in m.get('IdentificationList'):
                temp_model = AddAiotPersonTableItemRequestPersonTableItemIdentificationList()
                self.identification_list.append(temp_model.from_map(k))
        if m.get('ImageNum') is not None:
            self.image_num = m.get('ImageNum')
        self.image_list = []
        if m.get('ImageList') is not None:
            for k in m.get('ImageList'):
                temp_model = AddAiotPersonTableItemRequestPersonTableItemImageList()
                self.image_list.append(temp_model.from_map(k))
        return self


class AddAiotPersonTableItemRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        person_table_id: str = None,
        person_table_item: AddAiotPersonTableItemRequestPersonTableItem = None,
    ):
        self.id = id
        self.person_table_id = person_table_id
        self.person_table_item = person_table_item

    def validate(self):
        if self.person_table_item:
            self.person_table_item.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.person_table_id is not None:
            result['PersonTableId'] = self.person_table_id
        if self.person_table_item is not None:
            result['PersonTableItem'] = self.person_table_item.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PersonTableId') is not None:
            self.person_table_id = m.get('PersonTableId')
        if m.get('PersonTableItem') is not None:
            temp_model = AddAiotPersonTableItemRequestPersonTableItem()
            self.person_table_item = temp_model.from_map(m['PersonTableItem'])
        return self


class AddAiotPersonTableItemResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        person_table_item_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message
        self.person_table_item_id = person_table_item_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.person_table_item_id is not None:
            result['PersonTableItemId'] = self.person_table_item_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PersonTableItemId') is not None:
            self.person_table_item_id = m.get('PersonTableItemId')
        return self


class AddAiotPersonTableItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddAiotPersonTableItemResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddAiotPersonTableItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddAiotPersonTableItemsRequestPersonTableItemListIdentificationList(TeaModel):
    def __init__(
        self,
        type: int = None,
        number: str = None,
    ):
        self.type = type
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.number is not None:
            result['Number'] = self.number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        return self


class AddAiotPersonTableItemsRequestPersonTableItemListImageListFeatureInfo(TeaModel):
    def __init__(
        self,
        vendor: str = None,
        algorithm_version: str = None,
        algorithm_type: str = None,
        tab_ied: str = None,
        object_id: str = None,
        image_id: str = None,
        feature_data: str = None,
    ):
        self.vendor = vendor
        self.algorithm_version = algorithm_version
        self.algorithm_type = algorithm_type
        self.tab_ied = tab_ied
        self.object_id = object_id
        self.image_id = image_id
        self.feature_data = feature_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.algorithm_version is not None:
            result['AlgorithmVersion'] = self.algorithm_version
        if self.algorithm_type is not None:
            result['AlgorithmType'] = self.algorithm_type
        if self.tab_ied is not None:
            result['TabIed'] = self.tab_ied
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.feature_data is not None:
            result['FeatureData'] = self.feature_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('AlgorithmVersion') is not None:
            self.algorithm_version = m.get('AlgorithmVersion')
        if m.get('AlgorithmType') is not None:
            self.algorithm_type = m.get('AlgorithmType')
        if m.get('TabIed') is not None:
            self.tab_ied = m.get('TabIed')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('FeatureData') is not None:
            self.feature_data = m.get('FeatureData')
        return self


class AddAiotPersonTableItemsRequestPersonTableItemListImageList(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        event_sort: str = None,
        device_id: str = None,
        storage_path: str = None,
        size: int = None,
        type: str = None,
        file_format: str = None,
        shot_time: str = None,
        width: int = None,
        height: int = None,
        data: str = None,
        feature_info: AddAiotPersonTableItemsRequestPersonTableItemListImageListFeatureInfo = None,
    ):
        self.image_id = image_id
        self.event_sort = event_sort
        self.device_id = device_id
        self.storage_path = storage_path
        self.size = size
        self.type = type
        self.file_format = file_format
        self.shot_time = shot_time
        self.width = width
        self.height = height
        self.data = data
        self.feature_info = feature_info

    def validate(self):
        if self.feature_info:
            self.feature_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.event_sort is not None:
            result['EventSort'] = self.event_sort
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.storage_path is not None:
            result['StoragePath'] = self.storage_path
        if self.size is not None:
            result['Size'] = self.size
        if self.type is not None:
            result['Type'] = self.type
        if self.file_format is not None:
            result['FileFormat'] = self.file_format
        if self.shot_time is not None:
            result['ShotTime'] = self.shot_time
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.data is not None:
            result['Data'] = self.data
        if self.feature_info is not None:
            result['FeatureInfo'] = self.feature_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('EventSort') is not None:
            self.event_sort = m.get('EventSort')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('StoragePath') is not None:
            self.storage_path = m.get('StoragePath')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')
        if m.get('ShotTime') is not None:
            self.shot_time = m.get('ShotTime')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('FeatureInfo') is not None:
            temp_model = AddAiotPersonTableItemsRequestPersonTableItemListImageListFeatureInfo()
            self.feature_info = temp_model.from_map(m['FeatureInfo'])
        return self


class AddAiotPersonTableItemsRequestPersonTableItemList(TeaModel):
    def __init__(
        self,
        person_id: str = None,
        person_code: str = None,
        person_name: str = None,
        remarks: str = None,
        identification_num: int = None,
        identification_list: List[AddAiotPersonTableItemsRequestPersonTableItemListIdentificationList] = None,
        image_num: int = None,
        image_list: List[AddAiotPersonTableItemsRequestPersonTableItemListImageList] = None,
    ):
        self.person_id = person_id
        self.person_code = person_code
        self.person_name = person_name
        self.remarks = remarks
        self.identification_num = identification_num
        self.identification_list = identification_list
        self.image_num = image_num
        self.image_list = image_list

    def validate(self):
        if self.identification_list:
            for k in self.identification_list:
                if k:
                    k.validate()
        if self.image_list:
            for k in self.image_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.person_code is not None:
            result['PersonCode'] = self.person_code
        if self.person_name is not None:
            result['PersonName'] = self.person_name
        if self.remarks is not None:
            result['Remarks'] = self.remarks
        if self.identification_num is not None:
            result['IdentificationNum'] = self.identification_num
        result['IdentificationList'] = []
        if self.identification_list is not None:
            for k in self.identification_list:
                result['IdentificationList'].append(k.to_map() if k else None)
        if self.image_num is not None:
            result['ImageNum'] = self.image_num
        result['ImageList'] = []
        if self.image_list is not None:
            for k in self.image_list:
                result['ImageList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('PersonCode') is not None:
            self.person_code = m.get('PersonCode')
        if m.get('PersonName') is not None:
            self.person_name = m.get('PersonName')
        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')
        if m.get('IdentificationNum') is not None:
            self.identification_num = m.get('IdentificationNum')
        self.identification_list = []
        if m.get('IdentificationList') is not None:
            for k in m.get('IdentificationList'):
                temp_model = AddAiotPersonTableItemsRequestPersonTableItemListIdentificationList()
                self.identification_list.append(temp_model.from_map(k))
        if m.get('ImageNum') is not None:
            self.image_num = m.get('ImageNum')
        self.image_list = []
        if m.get('ImageList') is not None:
            for k in m.get('ImageList'):
                temp_model = AddAiotPersonTableItemsRequestPersonTableItemListImageList()
                self.image_list.append(temp_model.from_map(k))
        return self


class AddAiotPersonTableItemsRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        person_table_id: str = None,
        person_table_item_list: List[AddAiotPersonTableItemsRequestPersonTableItemList] = None,
    ):
        self.id = id
        self.person_table_id = person_table_id
        self.person_table_item_list = person_table_item_list

    def validate(self):
        if self.person_table_item_list:
            for k in self.person_table_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.person_table_id is not None:
            result['PersonTableId'] = self.person_table_id
        result['PersonTableItemList'] = []
        if self.person_table_item_list is not None:
            for k in self.person_table_item_list:
                result['PersonTableItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PersonTableId') is not None:
            self.person_table_id = m.get('PersonTableId')
        self.person_table_item_list = []
        if m.get('PersonTableItemList') is not None:
            for k in m.get('PersonTableItemList'):
                temp_model = AddAiotPersonTableItemsRequestPersonTableItemList()
                self.person_table_item_list.append(temp_model.from_map(k))
        return self


class AddAiotPersonTableItemsResponseBodyResultList(TeaModel):
    def __init__(
        self,
        person_table_item_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.person_table_item_id = person_table_item_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.person_table_item_id is not None:
            result['PersonTableItemId'] = self.person_table_item_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PersonTableItemId') is not None:
            self.person_table_item_id = m.get('PersonTableItemId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AddAiotPersonTableItemsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        result_list: List[AddAiotPersonTableItemsResponseBodyResultList] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message
        self.result_list = result_list

    def validate(self):
        if self.result_list:
            for k in self.result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['ResultList'] = []
        if self.result_list is not None:
            for k in self.result_list:
                result['ResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.result_list = []
        if m.get('ResultList') is not None:
            for k in m.get('ResultList'):
                temp_model = AddAiotPersonTableItemsResponseBodyResultList()
                self.result_list.append(temp_model.from_map(k))
        return self


class AddAiotPersonTableItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddAiotPersonTableItemsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddAiotPersonTableItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddChannelRequest(TeaModel):
    def __init__(
        self,
        parent_device_gb_id: str = None,
    ):
        self.parent_device_gb_id = parent_device_gb_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_device_gb_id is not None:
            result['ParentDeviceGbId'] = self.parent_device_gb_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParentDeviceGbId') is not None:
            self.parent_device_gb_id = m.get('ParentDeviceGbId')
        return self


class AddChannelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        data: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.message = message
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class AddChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddChannelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddDataSourceRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        data_source_name: str = None,
        data_source_type: str = None,
        description: str = None,
        file_retention_days: int = None,
    ):
        self.corp_id = corp_id
        self.data_source_name = data_source_name
        self.data_source_type = data_source_type
        self.description = description
        self.file_retention_days = file_retention_days

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.description is not None:
            result['Description'] = self.description
        if self.file_retention_days is not None:
            result['FileRetentionDays'] = self.file_retention_days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileRetentionDays') is not None:
            self.file_retention_days = m.get('FileRetentionDays')
        return self


class AddDataSourceResponseBodyData(TeaModel):
    def __init__(
        self,
        kafka_topic: str = None,
        data_source_id: str = None,
        oss_path: str = None,
    ):
        self.kafka_topic = kafka_topic
        self.data_source_id = data_source_id
        self.oss_path = oss_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kafka_topic is not None:
            result['KafkaTopic'] = self.kafka_topic
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KafkaTopic') is not None:
            self.kafka_topic = m.get('KafkaTopic')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        return self


class AddDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        data: AddDataSourceResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = AddDataSourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class AddDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddDataSourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddDeviceRequest(TeaModel):
    def __init__(
        self,
        gb_id: str = None,
        device_name: str = None,
        device_type: str = None,
        device_address: str = None,
        device_site: str = None,
        device_direction: str = None,
        device_resolution: str = None,
        bit_rate: str = None,
        corp_id: str = None,
        vendor: str = None,
    ):
        self.gb_id = gb_id
        self.device_name = device_name
        self.device_type = device_type
        self.device_address = device_address
        self.device_site = device_site
        self.device_direction = device_direction
        self.device_resolution = device_resolution
        self.bit_rate = bit_rate
        self.corp_id = corp_id
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.device_address is not None:
            result['DeviceAddress'] = self.device_address
        if self.device_site is not None:
            result['DeviceSite'] = self.device_site
        if self.device_direction is not None:
            result['DeviceDirection'] = self.device_direction
        if self.device_resolution is not None:
            result['DeviceResolution'] = self.device_resolution
        if self.bit_rate is not None:
            result['BitRate'] = self.bit_rate
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('DeviceAddress') is not None:
            self.device_address = m.get('DeviceAddress')
        if m.get('DeviceSite') is not None:
            self.device_site = m.get('DeviceSite')
        if m.get('DeviceDirection') is not None:
            self.device_direction = m.get('DeviceDirection')
        if m.get('DeviceResolution') is not None:
            self.device_resolution = m.get('DeviceResolution')
        if m.get('BitRate') is not None:
            self.bit_rate = m.get('BitRate')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class AddDeviceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class AddDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddDoubleVerificationGroupsRequestDoubleVerificationGroupListPersonIdList(TeaModel):
    def __init__(
        self,
        person_table_id: str = None,
        person_id: str = None,
    ):
        self.person_table_id = person_table_id
        self.person_id = person_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.person_table_id is not None:
            result['PersonTableId'] = self.person_table_id
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PersonTableId') is not None:
            self.person_table_id = m.get('PersonTableId')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        return self


class AddDoubleVerificationGroupsRequestDoubleVerificationGroupList(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        interval: int = None,
        member_number: int = None,
        person_id_list: List[AddDoubleVerificationGroupsRequestDoubleVerificationGroupListPersonIdList] = None,
    ):
        self.group_id = group_id
        self.interval = interval
        self.member_number = member_number
        self.person_id_list = person_id_list

    def validate(self):
        if self.person_id_list:
            for k in self.person_id_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.member_number is not None:
            result['MemberNumber'] = self.member_number
        result['PersonIdList'] = []
        if self.person_id_list is not None:
            for k in self.person_id_list:
                result['PersonIdList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('MemberNumber') is not None:
            self.member_number = m.get('MemberNumber')
        self.person_id_list = []
        if m.get('PersonIdList') is not None:
            for k in m.get('PersonIdList'):
                temp_model = AddDoubleVerificationGroupsRequestDoubleVerificationGroupListPersonIdList()
                self.person_id_list.append(temp_model.from_map(k))
        return self


class AddDoubleVerificationGroupsRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        double_verification_group_list: List[AddDoubleVerificationGroupsRequestDoubleVerificationGroupList] = None,
    ):
        self.id = id
        self.double_verification_group_list = double_verification_group_list

    def validate(self):
        if self.double_verification_group_list:
            for k in self.double_verification_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        result['DoubleVerificationGroupList'] = []
        if self.double_verification_group_list is not None:
            for k in self.double_verification_group_list:
                result['DoubleVerificationGroupList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.double_verification_group_list = []
        if m.get('DoubleVerificationGroupList') is not None:
            for k in m.get('DoubleVerificationGroupList'):
                temp_model = AddDoubleVerificationGroupsRequestDoubleVerificationGroupList()
                self.double_verification_group_list.append(temp_model.from_map(k))
        return self


class AddDoubleVerificationGroupsResponseBodyResultList(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.group_id = group_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AddDoubleVerificationGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        result_list: List[AddDoubleVerificationGroupsResponseBodyResultList] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message
        self.result_list = result_list

    def validate(self):
        if self.result_list:
            for k in self.result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['ResultList'] = []
        if self.result_list is not None:
            for k in self.result_list:
                result['ResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.result_list = []
        if m.get('ResultList') is not None:
            for k in m.get('ResultList'):
                temp_model = AddDoubleVerificationGroupsResponseBodyResultList()
                self.result_list.append(temp_model.from_map(k))
        return self


class AddDoubleVerificationGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddDoubleVerificationGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddDoubleVerificationGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddMonitorRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        monitor_type: str = None,
        description: str = None,
        batch_indicator: int = None,
        algorithm_vendor: str = None,
        notifier_type: str = None,
        notifier_url: str = None,
        notifier_app_secret: str = None,
        notifier_time_out: int = None,
        notifier_extend_values: str = None,
    ):
        self.corp_id = corp_id
        self.monitor_type = monitor_type
        self.description = description
        self.batch_indicator = batch_indicator
        self.algorithm_vendor = algorithm_vendor
        self.notifier_type = notifier_type
        self.notifier_url = notifier_url
        self.notifier_app_secret = notifier_app_secret
        self.notifier_time_out = notifier_time_out
        self.notifier_extend_values = notifier_extend_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.monitor_type is not None:
            result['MonitorType'] = self.monitor_type
        if self.description is not None:
            result['Description'] = self.description
        if self.batch_indicator is not None:
            result['BatchIndicator'] = self.batch_indicator
        if self.algorithm_vendor is not None:
            result['AlgorithmVendor'] = self.algorithm_vendor
        if self.notifier_type is not None:
            result['NotifierType'] = self.notifier_type
        if self.notifier_url is not None:
            result['NotifierUrl'] = self.notifier_url
        if self.notifier_app_secret is not None:
            result['NotifierAppSecret'] = self.notifier_app_secret
        if self.notifier_time_out is not None:
            result['NotifierTimeOut'] = self.notifier_time_out
        if self.notifier_extend_values is not None:
            result['NotifierExtendValues'] = self.notifier_extend_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('MonitorType') is not None:
            self.monitor_type = m.get('MonitorType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('BatchIndicator') is not None:
            self.batch_indicator = m.get('BatchIndicator')
        if m.get('AlgorithmVendor') is not None:
            self.algorithm_vendor = m.get('AlgorithmVendor')
        if m.get('NotifierType') is not None:
            self.notifier_type = m.get('NotifierType')
        if m.get('NotifierUrl') is not None:
            self.notifier_url = m.get('NotifierUrl')
        if m.get('NotifierAppSecret') is not None:
            self.notifier_app_secret = m.get('NotifierAppSecret')
        if m.get('NotifierTimeOut') is not None:
            self.notifier_time_out = m.get('NotifierTimeOut')
        if m.get('NotifierExtendValues') is not None:
            self.notifier_extend_values = m.get('NotifierExtendValues')
        return self


class AddMonitorResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class AddMonitorResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: AddMonitorResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AddMonitorResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class AddMonitorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddMonitorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddProfileRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        isv_sub_id: str = None,
        name: str = None,
        catalog_id: int = None,
        id_number: str = None,
        face_url: str = None,
        live_address: str = None,
        gender: int = None,
        plate_no: str = None,
        phone_no: str = None,
        scene_type: str = None,
        biz_id: str = None,
    ):
        self.corp_id = corp_id
        self.isv_sub_id = isv_sub_id
        self.name = name
        self.catalog_id = catalog_id
        self.id_number = id_number
        self.face_url = face_url
        self.live_address = live_address
        self.gender = gender
        self.plate_no = plate_no
        self.phone_no = phone_no
        self.scene_type = scene_type
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.name is not None:
            result['Name'] = self.name
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.id_number is not None:
            result['IdNumber'] = self.id_number
        if self.face_url is not None:
            result['FaceUrl'] = self.face_url
        if self.live_address is not None:
            result['LiveAddress'] = self.live_address
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.plate_no is not None:
            result['PlateNo'] = self.plate_no
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('IdNumber') is not None:
            self.id_number = m.get('IdNumber')
        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')
        if m.get('LiveAddress') is not None:
            self.live_address = m.get('LiveAddress')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('PlateNo') is not None:
            self.plate_no = m.get('PlateNo')
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class AddProfileResponseBodyData(TeaModel):
    def __init__(
        self,
        catalog_id: int = None,
        profile_id: int = None,
        isv_sub_id: str = None,
        gender: str = None,
        biz_id: str = None,
        id_number: str = None,
        scene_type: str = None,
        phone_no: str = None,
        face_url: str = None,
        live_address: str = None,
        name: str = None,
        plate_no: str = None,
    ):
        self.catalog_id = catalog_id
        self.profile_id = profile_id
        self.isv_sub_id = isv_sub_id
        self.gender = gender
        self.biz_id = biz_id
        self.id_number = id_number
        self.scene_type = scene_type
        self.phone_no = phone_no
        self.face_url = face_url
        self.live_address = live_address
        self.name = name
        self.plate_no = plate_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.profile_id is not None:
            result['ProfileId'] = self.profile_id
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.id_number is not None:
            result['IdNumber'] = self.id_number
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        if self.face_url is not None:
            result['FaceUrl'] = self.face_url
        if self.live_address is not None:
            result['LiveAddress'] = self.live_address
        if self.name is not None:
            result['Name'] = self.name
        if self.plate_no is not None:
            result['PlateNo'] = self.plate_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('ProfileId') is not None:
            self.profile_id = m.get('ProfileId')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('IdNumber') is not None:
            self.id_number = m.get('IdNumber')
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')
        if m.get('LiveAddress') is not None:
            self.live_address = m.get('LiveAddress')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PlateNo') is not None:
            self.plate_no = m.get('PlateNo')
        return self


class AddProfileResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: AddProfileResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AddProfileResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class AddProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddProfileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddProfileCatalogRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        isv_sub_id: str = None,
        catalog_name: str = None,
        parent_catalog_id: int = None,
    ):
        self.corp_id = corp_id
        self.isv_sub_id = isv_sub_id
        self.catalog_name = catalog_name
        self.parent_catalog_id = parent_catalog_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.parent_catalog_id is not None:
            result['ParentCatalogId'] = self.parent_catalog_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('ParentCatalogId') is not None:
            self.parent_catalog_id = m.get('ParentCatalogId')
        return self


class AddProfileCatalogResponseBodyData(TeaModel):
    def __init__(
        self,
        catalog_id: int = None,
        catalog_name: str = None,
        isv_sub_id: str = None,
    ):
        self.catalog_id = catalog_id
        self.catalog_name = catalog_name
        self.isv_sub_id = isv_sub_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        return self


class AddProfileCatalogResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: AddProfileCatalogResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AddProfileCatalogResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class AddProfileCatalogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddProfileCatalogResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddProfileCatalogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindCorpGroupRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        corp_group_id: str = None,
    ):
        self.corp_id = corp_id
        self.corp_group_id = corp_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.corp_group_id is not None:
            result['CorpGroupId'] = self.corp_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('CorpGroupId') is not None:
            self.corp_group_id = m.get('CorpGroupId')
        return self


class BindCorpGroupResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BindCorpGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BindCorpGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BindCorpGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindPersonRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        isv_sub_id: str = None,
        person_matching_rate: str = None,
        person_id: str = None,
        profile_id: int = None,
    ):
        self.corp_id = corp_id
        self.isv_sub_id = isv_sub_id
        self.person_matching_rate = person_matching_rate
        self.person_id = person_id
        self.profile_id = profile_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.person_matching_rate is not None:
            result['PersonMatchingRate'] = self.person_matching_rate
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.profile_id is not None:
            result['ProfileId'] = self.profile_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('PersonMatchingRate') is not None:
            self.person_matching_rate = m.get('PersonMatchingRate')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('ProfileId') is not None:
            self.profile_id = m.get('ProfileId')
        return self


class BindPersonResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: bool = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class BindPersonResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BindPersonResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BindPersonResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindUserRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        isv_sub_id: str = None,
        matching_rate: str = None,
        person_id: str = None,
        user_id: int = None,
    ):
        self.corp_id = corp_id
        self.isv_sub_id = isv_sub_id
        self.matching_rate = matching_rate
        self.person_id = person_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.matching_rate is not None:
            result['MatchingRate'] = self.matching_rate
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('MatchingRate') is not None:
            self.matching_rate = m.get('MatchingRate')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class BindUserResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: bool = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class BindUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BindUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BindUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ControlAiotDeviceRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        command_type: int = None,
        gate_ctl_status: int = None,
        barrier_command: int = None,
        reboot_device: str = None,
        upgrade_file_url: str = None,
        associated_device_id: str = None,
        single_interval: int = None,
        super_password: str = None,
        double_verification_group_enabled: str = None,
    ):
        self.id = id
        self.name = name
        self.command_type = command_type
        self.gate_ctl_status = gate_ctl_status
        self.barrier_command = barrier_command
        self.reboot_device = reboot_device
        self.upgrade_file_url = upgrade_file_url
        self.associated_device_id = associated_device_id
        self.single_interval = single_interval
        self.super_password = super_password
        self.double_verification_group_enabled = double_verification_group_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.command_type is not None:
            result['CommandType'] = self.command_type
        if self.gate_ctl_status is not None:
            result['GateCtlStatus'] = self.gate_ctl_status
        if self.barrier_command is not None:
            result['BarrierCommand'] = self.barrier_command
        if self.reboot_device is not None:
            result['RebootDevice'] = self.reboot_device
        if self.upgrade_file_url is not None:
            result['UpgradeFileURL'] = self.upgrade_file_url
        if self.associated_device_id is not None:
            result['AssociatedDeviceId'] = self.associated_device_id
        if self.single_interval is not None:
            result['SingleInterval'] = self.single_interval
        if self.super_password is not None:
            result['SuperPassword'] = self.super_password
        if self.double_verification_group_enabled is not None:
            result['DoubleVerificationGroupEnabled'] = self.double_verification_group_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CommandType') is not None:
            self.command_type = m.get('CommandType')
        if m.get('GateCtlStatus') is not None:
            self.gate_ctl_status = m.get('GateCtlStatus')
        if m.get('BarrierCommand') is not None:
            self.barrier_command = m.get('BarrierCommand')
        if m.get('RebootDevice') is not None:
            self.reboot_device = m.get('RebootDevice')
        if m.get('UpgradeFileURL') is not None:
            self.upgrade_file_url = m.get('UpgradeFileURL')
        if m.get('AssociatedDeviceId') is not None:
            self.associated_device_id = m.get('AssociatedDeviceId')
        if m.get('SingleInterval') is not None:
            self.single_interval = m.get('SingleInterval')
        if m.get('SuperPassword') is not None:
            self.super_password = m.get('SuperPassword')
        if m.get('DoubleVerificationGroupEnabled') is not None:
            self.double_verification_group_enabled = m.get('DoubleVerificationGroupEnabled')
        return self


class ControlAiotDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.message = message
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ControlAiotDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ControlAiotDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ControlAiotDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCorpRequest(TeaModel):
    def __init__(
        self,
        corp_name: str = None,
        app_name: str = None,
        parent_corp_id: str = None,
        description: str = None,
        algorithm_type: str = None,
        isv_sub_id: str = None,
        icon_path: str = None,
    ):
        self.corp_name = corp_name
        self.app_name = app_name
        self.parent_corp_id = parent_corp_id
        self.description = description
        self.algorithm_type = algorithm_type
        self.isv_sub_id = isv_sub_id
        self.icon_path = icon_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_name is not None:
            result['CorpName'] = self.corp_name
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.parent_corp_id is not None:
            result['ParentCorpId'] = self.parent_corp_id
        if self.description is not None:
            result['Description'] = self.description
        if self.algorithm_type is not None:
            result['AlgorithmType'] = self.algorithm_type
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.icon_path is not None:
            result['IconPath'] = self.icon_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpName') is not None:
            self.corp_name = m.get('CorpName')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ParentCorpId') is not None:
            self.parent_corp_id = m.get('ParentCorpId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AlgorithmType') is not None:
            self.algorithm_type = m.get('AlgorithmType')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('IconPath') is not None:
            self.icon_path = m.get('IconPath')
        return self


class CreateCorpResponseBody(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.corp_id = corp_id
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreateCorpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCorpResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateCorpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCorpGroupRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        group_id: str = None,
        client_token: str = None,
    ):
        self.corp_id = corp_id
        self.group_id = group_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateCorpGroupResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateCorpGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCorpGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateCorpGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDeviceRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        city_code: str = None,
        longitude: str = None,
        data_source_type: str = None,
        device_name: str = None,
        device_vendor: str = None,
        device_group_name: str = None,
        latitude: str = None,
        device_address: str = None,
        device_type: str = None,
        sub_device_count: int = None,
        device_model: str = None,
        gb_id: str = None,
        file_path: str = None,
    ):
        self.corp_id = corp_id
        self.city_code = city_code
        self.longitude = longitude
        self.data_source_type = data_source_type
        self.device_name = device_name
        self.device_vendor = device_vendor
        self.device_group_name = device_group_name
        self.latitude = latitude
        self.device_address = device_address
        self.device_type = device_type
        self.sub_device_count = sub_device_count
        self.device_model = device_model
        self.gb_id = gb_id
        self.file_path = file_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.city_code is not None:
            result['CityCode'] = self.city_code
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_vendor is not None:
            result['DeviceVendor'] = self.device_vendor
        if self.device_group_name is not None:
            result['DeviceGroupName'] = self.device_group_name
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.device_address is not None:
            result['DeviceAddress'] = self.device_address
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.sub_device_count is not None:
            result['SubDeviceCount'] = self.sub_device_count
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceVendor') is not None:
            self.device_vendor = m.get('DeviceVendor')
        if m.get('DeviceGroupName') is not None:
            self.device_group_name = m.get('DeviceGroupName')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('DeviceAddress') is not None:
            self.device_address = m.get('DeviceAddress')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('SubDeviceCount') is not None:
            self.sub_device_count = m.get('SubDeviceCount')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        return self


class CreateDeviceResponseBodyDataSubDeviceSipInfo(TeaModel):
    def __init__(
        self,
        sunday_capture_strategy: str = None,
        monday_capture_strategy: str = None,
        channel_gb_id: str = None,
        friday_capture_strategy: str = None,
        tuesday_capture_strategy: str = None,
        wednesday_capture_strategy: str = None,
        thursday_capture_strategy: str = None,
        saturday_capture_strategy: str = None,
    ):
        self.sunday_capture_strategy = sunday_capture_strategy
        self.monday_capture_strategy = monday_capture_strategy
        self.channel_gb_id = channel_gb_id
        self.friday_capture_strategy = friday_capture_strategy
        self.tuesday_capture_strategy = tuesday_capture_strategy
        self.wednesday_capture_strategy = wednesday_capture_strategy
        self.thursday_capture_strategy = thursday_capture_strategy
        self.saturday_capture_strategy = saturday_capture_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sunday_capture_strategy is not None:
            result['SundayCaptureStrategy'] = self.sunday_capture_strategy
        if self.monday_capture_strategy is not None:
            result['MondayCaptureStrategy'] = self.monday_capture_strategy
        if self.channel_gb_id is not None:
            result['ChannelGbId'] = self.channel_gb_id
        if self.friday_capture_strategy is not None:
            result['FridayCaptureStrategy'] = self.friday_capture_strategy
        if self.tuesday_capture_strategy is not None:
            result['TuesdayCaptureStrategy'] = self.tuesday_capture_strategy
        if self.wednesday_capture_strategy is not None:
            result['WednesdayCaptureStrategy'] = self.wednesday_capture_strategy
        if self.thursday_capture_strategy is not None:
            result['ThursdayCaptureStrategy'] = self.thursday_capture_strategy
        if self.saturday_capture_strategy is not None:
            result['SaturdayCaptureStrategy'] = self.saturday_capture_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SundayCaptureStrategy') is not None:
            self.sunday_capture_strategy = m.get('SundayCaptureStrategy')
        if m.get('MondayCaptureStrategy') is not None:
            self.monday_capture_strategy = m.get('MondayCaptureStrategy')
        if m.get('ChannelGbId') is not None:
            self.channel_gb_id = m.get('ChannelGbId')
        if m.get('FridayCaptureStrategy') is not None:
            self.friday_capture_strategy = m.get('FridayCaptureStrategy')
        if m.get('TuesdayCaptureStrategy') is not None:
            self.tuesday_capture_strategy = m.get('TuesdayCaptureStrategy')
        if m.get('WednesdayCaptureStrategy') is not None:
            self.wednesday_capture_strategy = m.get('WednesdayCaptureStrategy')
        if m.get('ThursdayCaptureStrategy') is not None:
            self.thursday_capture_strategy = m.get('ThursdayCaptureStrategy')
        if m.get('SaturdayCaptureStrategy') is not None:
            self.saturday_capture_strategy = m.get('SaturdayCaptureStrategy')
        return self


class CreateDeviceResponseBodyData(TeaModel):
    def __init__(
        self,
        sip_reaml: str = None,
        sip_ip: str = None,
        sip_device_gb_id: str = None,
        device_code: str = None,
        sip_port: str = None,
        sip_gb_id: str = None,
        sip_password: str = None,
        sub_device_sip_info: List[CreateDeviceResponseBodyDataSubDeviceSipInfo] = None,
    ):
        self.sip_reaml = sip_reaml
        self.sip_ip = sip_ip
        self.sip_device_gb_id = sip_device_gb_id
        self.device_code = device_code
        self.sip_port = sip_port
        self.sip_gb_id = sip_gb_id
        self.sip_password = sip_password
        self.sub_device_sip_info = sub_device_sip_info

    def validate(self):
        if self.sub_device_sip_info:
            for k in self.sub_device_sip_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sip_reaml is not None:
            result['SipReaml'] = self.sip_reaml
        if self.sip_ip is not None:
            result['SipIp'] = self.sip_ip
        if self.sip_device_gb_id is not None:
            result['SipDeviceGbId'] = self.sip_device_gb_id
        if self.device_code is not None:
            result['DeviceCode'] = self.device_code
        if self.sip_port is not None:
            result['SipPort'] = self.sip_port
        if self.sip_gb_id is not None:
            result['SipGbId'] = self.sip_gb_id
        if self.sip_password is not None:
            result['SipPassword'] = self.sip_password
        result['SubDeviceSipInfo'] = []
        if self.sub_device_sip_info is not None:
            for k in self.sub_device_sip_info:
                result['SubDeviceSipInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SipReaml') is not None:
            self.sip_reaml = m.get('SipReaml')
        if m.get('SipIp') is not None:
            self.sip_ip = m.get('SipIp')
        if m.get('SipDeviceGbId') is not None:
            self.sip_device_gb_id = m.get('SipDeviceGbId')
        if m.get('DeviceCode') is not None:
            self.device_code = m.get('DeviceCode')
        if m.get('SipPort') is not None:
            self.sip_port = m.get('SipPort')
        if m.get('SipGbId') is not None:
            self.sip_gb_id = m.get('SipGbId')
        if m.get('SipPassword') is not None:
            self.sip_password = m.get('SipPassword')
        self.sub_device_sip_info = []
        if m.get('SubDeviceSipInfo') is not None:
            for k in m.get('SubDeviceSipInfo'):
                temp_model = CreateDeviceResponseBodyDataSubDeviceSipInfo()
                self.sub_device_sip_info.append(temp_model.from_map(k))
        return self


class CreateDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        data: CreateDeviceResponseBodyData = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = CreateDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class CreateDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMarkerRequest(TeaModel):
    def __init__(
        self,
        algorithm_id: str = None,
        label_id: str = None,
        sample_id: str = None,
        content: str = None,
    ):
        self.algorithm_id = algorithm_id
        self.label_id = label_id
        self.sample_id = sample_id
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        if self.sample_id is not None:
            result['SampleId'] = self.sample_id
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        if m.get('SampleId') is not None:
            self.sample_id = m.get('SampleId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class CreateMarkerResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateMarkerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        data: CreateMarkerResponseBodyData = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = CreateMarkerResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class CreateMarkerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateMarkerResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateMarkerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSampleRequest(TeaModel):
    def __init__(
        self,
        algorithm_id: str = None,
        sample_list: str = None,
    ):
        self.algorithm_id = algorithm_id
        self.sample_list = sample_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.sample_list is not None:
            result['SampleList'] = self.sample_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('SampleList') is not None:
            self.sample_list = m.get('SampleList')
        return self


class CreateSampleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class CreateSampleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSampleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSampleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScanDeviceRequest(TeaModel):
    def __init__(
        self,
        access_point_vendor: str = None,
        access_protocol_type: str = None,
        audio_enable: str = None,
        city_code: str = None,
        corp_id: str = None,
        device_address: str = None,
        device_direction: str = None,
        device_name: str = None,
        device_rate: str = None,
        device_resolution: str = None,
        device_site: str = None,
        device_sn: str = None,
        device_type: str = None,
        encode_format: str = None,
        frame_rate: str = None,
        gb_id: str = None,
        gov_length: str = None,
        latitude: str = None,
        longitude: str = None,
        osdtime_enable: str = None,
        osdtime_type: str = None,
        osdtime_x: str = None,
        osdtime_y: str = None,
        vendor: str = None,
        data_source_type: str = None,
        sub_device_count: int = None,
        device_model: str = None,
    ):
        self.access_point_vendor = access_point_vendor
        self.access_protocol_type = access_protocol_type
        self.audio_enable = audio_enable
        self.city_code = city_code
        self.corp_id = corp_id
        self.device_address = device_address
        self.device_direction = device_direction
        self.device_name = device_name
        self.device_rate = device_rate
        self.device_resolution = device_resolution
        self.device_site = device_site
        self.device_sn = device_sn
        self.device_type = device_type
        self.encode_format = encode_format
        self.frame_rate = frame_rate
        self.gb_id = gb_id
        self.gov_length = gov_length
        self.latitude = latitude
        self.longitude = longitude
        self.osdtime_enable = osdtime_enable
        self.osdtime_type = osdtime_type
        self.osdtime_x = osdtime_x
        self.osdtime_y = osdtime_y
        self.vendor = vendor
        self.data_source_type = data_source_type
        self.sub_device_count = sub_device_count
        self.device_model = device_model

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_point_vendor is not None:
            result['AccessPointVendor'] = self.access_point_vendor
        if self.access_protocol_type is not None:
            result['AccessProtocolType'] = self.access_protocol_type
        if self.audio_enable is not None:
            result['AudioEnable'] = self.audio_enable
        if self.city_code is not None:
            result['CityCode'] = self.city_code
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.device_address is not None:
            result['DeviceAddress'] = self.device_address
        if self.device_direction is not None:
            result['DeviceDirection'] = self.device_direction
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_rate is not None:
            result['DeviceRate'] = self.device_rate
        if self.device_resolution is not None:
            result['DeviceResolution'] = self.device_resolution
        if self.device_site is not None:
            result['DeviceSite'] = self.device_site
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.encode_format is not None:
            result['EncodeFormat'] = self.encode_format
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.gov_length is not None:
            result['GovLength'] = self.gov_length
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.osdtime_enable is not None:
            result['OSDTimeEnable'] = self.osdtime_enable
        if self.osdtime_type is not None:
            result['OSDTimeType'] = self.osdtime_type
        if self.osdtime_x is not None:
            result['OSDTimeX'] = self.osdtime_x
        if self.osdtime_y is not None:
            result['OSDTimeY'] = self.osdtime_y
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.sub_device_count is not None:
            result['SubDeviceCount'] = self.sub_device_count
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointVendor') is not None:
            self.access_point_vendor = m.get('AccessPointVendor')
        if m.get('AccessProtocolType') is not None:
            self.access_protocol_type = m.get('AccessProtocolType')
        if m.get('AudioEnable') is not None:
            self.audio_enable = m.get('AudioEnable')
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('DeviceAddress') is not None:
            self.device_address = m.get('DeviceAddress')
        if m.get('DeviceDirection') is not None:
            self.device_direction = m.get('DeviceDirection')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceRate') is not None:
            self.device_rate = m.get('DeviceRate')
        if m.get('DeviceResolution') is not None:
            self.device_resolution = m.get('DeviceResolution')
        if m.get('DeviceSite') is not None:
            self.device_site = m.get('DeviceSite')
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('EncodeFormat') is not None:
            self.encode_format = m.get('EncodeFormat')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('GovLength') is not None:
            self.gov_length = m.get('GovLength')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('OSDTimeEnable') is not None:
            self.osdtime_enable = m.get('OSDTimeEnable')
        if m.get('OSDTimeType') is not None:
            self.osdtime_type = m.get('OSDTimeType')
        if m.get('OSDTimeX') is not None:
            self.osdtime_x = m.get('OSDTimeX')
        if m.get('OSDTimeY') is not None:
            self.osdtime_y = m.get('OSDTimeY')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('SubDeviceCount') is not None:
            self.sub_device_count = m.get('SubDeviceCount')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        return self


class CreateScanDeviceResponseBodyDataSubDeviceSipInfo(TeaModel):
    def __init__(
        self,
        sunday_capture_strategy: str = None,
        channel_gb_id: str = None,
        monday_capture_strategy: str = None,
        friday_capture_strategy: str = None,
        tuesday_capture_strategy: str = None,
        wednesday_capture_strategy: str = None,
        thursday_capture_strategy: str = None,
        saturday_capture_strategy: str = None,
    ):
        self.sunday_capture_strategy = sunday_capture_strategy
        self.channel_gb_id = channel_gb_id
        self.monday_capture_strategy = monday_capture_strategy
        self.friday_capture_strategy = friday_capture_strategy
        self.tuesday_capture_strategy = tuesday_capture_strategy
        self.wednesday_capture_strategy = wednesday_capture_strategy
        self.thursday_capture_strategy = thursday_capture_strategy
        self.saturday_capture_strategy = saturday_capture_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sunday_capture_strategy is not None:
            result['SundayCaptureStrategy'] = self.sunday_capture_strategy
        if self.channel_gb_id is not None:
            result['ChannelGbId'] = self.channel_gb_id
        if self.monday_capture_strategy is not None:
            result['MondayCaptureStrategy'] = self.monday_capture_strategy
        if self.friday_capture_strategy is not None:
            result['FridayCaptureStrategy'] = self.friday_capture_strategy
        if self.tuesday_capture_strategy is not None:
            result['TuesdayCaptureStrategy'] = self.tuesday_capture_strategy
        if self.wednesday_capture_strategy is not None:
            result['WednesdayCaptureStrategy'] = self.wednesday_capture_strategy
        if self.thursday_capture_strategy is not None:
            result['ThursdayCaptureStrategy'] = self.thursday_capture_strategy
        if self.saturday_capture_strategy is not None:
            result['SaturdayCaptureStrategy'] = self.saturday_capture_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SundayCaptureStrategy') is not None:
            self.sunday_capture_strategy = m.get('SundayCaptureStrategy')
        if m.get('ChannelGbId') is not None:
            self.channel_gb_id = m.get('ChannelGbId')
        if m.get('MondayCaptureStrategy') is not None:
            self.monday_capture_strategy = m.get('MondayCaptureStrategy')
        if m.get('FridayCaptureStrategy') is not None:
            self.friday_capture_strategy = m.get('FridayCaptureStrategy')
        if m.get('TuesdayCaptureStrategy') is not None:
            self.tuesday_capture_strategy = m.get('TuesdayCaptureStrategy')
        if m.get('WednesdayCaptureStrategy') is not None:
            self.wednesday_capture_strategy = m.get('WednesdayCaptureStrategy')
        if m.get('ThursdayCaptureStrategy') is not None:
            self.thursday_capture_strategy = m.get('ThursdayCaptureStrategy')
        if m.get('SaturdayCaptureStrategy') is not None:
            self.saturday_capture_strategy = m.get('SaturdayCaptureStrategy')
        return self


class CreateScanDeviceResponseBodyData(TeaModel):
    def __init__(
        self,
        sip_ip: str = None,
        sip_reaml: str = None,
        sip_device_gb_id: str = None,
        sip_port: str = None,
        device_code: str = None,
        sip_gb_id: str = None,
        sip_password: str = None,
        sub_device_sip_info: List[CreateScanDeviceResponseBodyDataSubDeviceSipInfo] = None,
        device_sn: str = None,
        corp_id: str = None,
    ):
        self.sip_ip = sip_ip
        self.sip_reaml = sip_reaml
        self.sip_device_gb_id = sip_device_gb_id
        self.sip_port = sip_port
        self.device_code = device_code
        self.sip_gb_id = sip_gb_id
        self.sip_password = sip_password
        self.sub_device_sip_info = sub_device_sip_info
        self.device_sn = device_sn
        self.corp_id = corp_id

    def validate(self):
        if self.sub_device_sip_info:
            for k in self.sub_device_sip_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sip_ip is not None:
            result['SipIp'] = self.sip_ip
        if self.sip_reaml is not None:
            result['SipReaml'] = self.sip_reaml
        if self.sip_device_gb_id is not None:
            result['SipDeviceGbId'] = self.sip_device_gb_id
        if self.sip_port is not None:
            result['SipPort'] = self.sip_port
        if self.device_code is not None:
            result['DeviceCode'] = self.device_code
        if self.sip_gb_id is not None:
            result['SipGbId'] = self.sip_gb_id
        if self.sip_password is not None:
            result['SipPassword'] = self.sip_password
        result['SubDeviceSipInfo'] = []
        if self.sub_device_sip_info is not None:
            for k in self.sub_device_sip_info:
                result['SubDeviceSipInfo'].append(k.to_map() if k else None)
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SipIp') is not None:
            self.sip_ip = m.get('SipIp')
        if m.get('SipReaml') is not None:
            self.sip_reaml = m.get('SipReaml')
        if m.get('SipDeviceGbId') is not None:
            self.sip_device_gb_id = m.get('SipDeviceGbId')
        if m.get('SipPort') is not None:
            self.sip_port = m.get('SipPort')
        if m.get('DeviceCode') is not None:
            self.device_code = m.get('DeviceCode')
        if m.get('SipGbId') is not None:
            self.sip_gb_id = m.get('SipGbId')
        if m.get('SipPassword') is not None:
            self.sip_password = m.get('SipPassword')
        self.sub_device_sip_info = []
        if m.get('SubDeviceSipInfo') is not None:
            for k in m.get('SubDeviceSipInfo'):
                temp_model = CreateScanDeviceResponseBodyDataSubDeviceSipInfo()
                self.sub_device_sip_info.append(temp_model.from_map(k))
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        return self


class CreateScanDeviceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: CreateScanDeviceResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateScanDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreateScanDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateScanDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateScanDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTrainLabelRequest(TeaModel):
    def __init__(
        self,
        algorithm_id: str = None,
        label_name: str = None,
    ):
        self.algorithm_id = algorithm_id
        self.label_name = label_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.label_name is not None:
            result['LabelName'] = self.label_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('LabelName') is not None:
            self.label_name = m.get('LabelName')
        return self


class CreateTrainLabelResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateTrainLabelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        data: CreateTrainLabelResponseBodyData = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = CreateTrainLabelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class CreateTrainLabelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTrainLabelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateTrainLabelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        isv_sub_id: str = None,
        user_name: str = None,
        user_group_id: int = None,
        id_number: str = None,
        face_image_url: str = None,
        address: str = None,
        age: int = None,
        gender: int = None,
        plate_no: str = None,
        phone_no: str = None,
        attachment: str = None,
        biz_id: str = None,
    ):
        self.corp_id = corp_id
        self.isv_sub_id = isv_sub_id
        self.user_name = user_name
        self.user_group_id = user_group_id
        self.id_number = id_number
        self.face_image_url = face_image_url
        self.address = address
        self.age = age
        self.gender = gender
        self.plate_no = plate_no
        self.phone_no = phone_no
        self.attachment = attachment
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.id_number is not None:
            result['IdNumber'] = self.id_number
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.address is not None:
            result['Address'] = self.address
        if self.age is not None:
            result['Age'] = self.age
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.plate_no is not None:
            result['PlateNo'] = self.plate_no
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        if self.attachment is not None:
            result['Attachment'] = self.attachment
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('IdNumber') is not None:
            self.id_number = m.get('IdNumber')
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('PlateNo') is not None:
            self.plate_no = m.get('PlateNo')
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        if m.get('Attachment') is not None:
            self.attachment = m.get('Attachment')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class CreateUserResponseBodyData(TeaModel):
    def __init__(
        self,
        gender: str = None,
        face_image_url: str = None,
        isv_sub_id: str = None,
        user_group_id: int = None,
        user_id: int = None,
        biz_id: str = None,
        attachment: str = None,
        age: str = None,
        id_number: str = None,
        phone_no: str = None,
        address: str = None,
        user_name: str = None,
        plate_no: str = None,
    ):
        self.gender = gender
        self.face_image_url = face_image_url
        self.isv_sub_id = isv_sub_id
        self.user_group_id = user_group_id
        self.user_id = user_id
        self.biz_id = biz_id
        self.attachment = attachment
        self.age = age
        self.id_number = id_number
        self.phone_no = phone_no
        self.address = address
        self.user_name = user_name
        self.plate_no = plate_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.attachment is not None:
            result['Attachment'] = self.attachment
        if self.age is not None:
            result['Age'] = self.age
        if self.id_number is not None:
            result['IdNumber'] = self.id_number
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        if self.address is not None:
            result['Address'] = self.address
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.plate_no is not None:
            result['PlateNo'] = self.plate_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Attachment') is not None:
            self.attachment = m.get('Attachment')
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('IdNumber') is not None:
            self.id_number = m.get('IdNumber')
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('PlateNo') is not None:
            self.plate_no = m.get('PlateNo')
        return self


class CreateUserResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: CreateUserResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateUserResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreateUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserGroupRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        isv_sub_id: str = None,
        user_group_name: str = None,
        parent_user_group_id: int = None,
    ):
        self.corp_id = corp_id
        self.isv_sub_id = isv_sub_id
        self.user_group_name = user_group_name
        self.parent_user_group_id = parent_user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        if self.parent_user_group_id is not None:
            result['ParentUserGroupId'] = self.parent_user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        if m.get('ParentUserGroupId') is not None:
            self.parent_user_group_id = m.get('ParentUserGroupId')
        return self


class CreateUserGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        isv_sub_id: str = None,
        user_group_id: int = None,
        user_group_name: str = None,
    ):
        self.isv_sub_id = isv_sub_id
        self.user_group_id = user_group_id
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        return self


class CreateUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: CreateUserGroupResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateUserGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreateUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateUserGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVideoComposeTaskRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        bucket_name: str = None,
        domain_name: str = None,
        image_file_names: str = None,
        audio_file_name: str = None,
        image_parameters: str = None,
        video_format: str = None,
        video_frame_rate: int = None,
    ):
        self.corp_id = corp_id
        self.bucket_name = bucket_name
        self.domain_name = domain_name
        self.image_file_names = image_file_names
        self.audio_file_name = audio_file_name
        self.image_parameters = image_parameters
        self.video_format = video_format
        self.video_frame_rate = video_frame_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.image_file_names is not None:
            result['ImageFileNames'] = self.image_file_names
        if self.audio_file_name is not None:
            result['AudioFileName'] = self.audio_file_name
        if self.image_parameters is not None:
            result['ImageParameters'] = self.image_parameters
        if self.video_format is not None:
            result['VideoFormat'] = self.video_format
        if self.video_frame_rate is not None:
            result['VideoFrameRate'] = self.video_frame_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ImageFileNames') is not None:
            self.image_file_names = m.get('ImageFileNames')
        if m.get('AudioFileName') is not None:
            self.audio_file_name = m.get('AudioFileName')
        if m.get('ImageParameters') is not None:
            self.image_parameters = m.get('ImageParameters')
        if m.get('VideoFormat') is not None:
            self.video_format = m.get('VideoFormat')
        if m.get('VideoFrameRate') is not None:
            self.video_frame_rate = m.get('VideoFrameRate')
        return self


class CreateVideoComposeTaskResponseBody(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        message: str = None,
        request_id: str = None,
        domain_name: str = None,
        code: str = None,
    ):
        self.bucket_name = bucket_name
        self.message = message
        self.request_id = request_id
        self.domain_name = domain_name
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreateVideoComposeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateVideoComposeTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateVideoComposeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVideoSummaryTaskRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        device_id: str = None,
        start_time_stamp: int = None,
        end_time_stamp: int = None,
        option_list: str = None,
        live_video_summary: str = None,
    ):
        self.corp_id = corp_id
        self.device_id = device_id
        self.start_time_stamp = start_time_stamp
        self.end_time_stamp = end_time_stamp
        self.option_list = option_list
        self.live_video_summary = live_video_summary

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.start_time_stamp is not None:
            result['StartTimeStamp'] = self.start_time_stamp
        if self.end_time_stamp is not None:
            result['EndTimeStamp'] = self.end_time_stamp
        if self.option_list is not None:
            result['OptionList'] = self.option_list
        if self.live_video_summary is not None:
            result['LiveVideoSummary'] = self.live_video_summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('StartTimeStamp') is not None:
            self.start_time_stamp = m.get('StartTimeStamp')
        if m.get('EndTimeStamp') is not None:
            self.end_time_stamp = m.get('EndTimeStamp')
        if m.get('OptionList') is not None:
            self.option_list = m.get('OptionList')
        if m.get('LiveVideoSummary') is not None:
            self.live_video_summary = m.get('LiveVideoSummary')
        return self


class CreateVideoSummaryTaskResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreateVideoSummaryTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateVideoSummaryTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateVideoSummaryTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAiotDeviceRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteAiotDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.message = message
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteAiotDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAiotDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAiotDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAiotPersonTableRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        person_table_id: str = None,
    ):
        self.id = id
        self.person_table_id = person_table_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.person_table_id is not None:
            result['PersonTableId'] = self.person_table_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PersonTableId') is not None:
            self.person_table_id = m.get('PersonTableId')
        return self


class DeleteAiotPersonTableResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DeleteAiotPersonTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAiotPersonTableResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAiotPersonTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAiotPersonTableItemRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        person_table_id: str = None,
        person_table_item_id: str = None,
    ):
        self.id = id
        self.person_table_id = person_table_id
        self.person_table_item_id = person_table_item_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.person_table_id is not None:
            result['PersonTableId'] = self.person_table_id
        if self.person_table_item_id is not None:
            result['PersonTableItemId'] = self.person_table_item_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PersonTableId') is not None:
            self.person_table_id = m.get('PersonTableId')
        if m.get('PersonTableItemId') is not None:
            self.person_table_item_id = m.get('PersonTableItemId')
        return self


class DeleteAiotPersonTableItemResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.message = message
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteAiotPersonTableItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAiotPersonTableItemResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAiotPersonTableItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteChannelRequest(TeaModel):
    def __init__(
        self,
        device_codes: str = None,
    ):
        self.device_codes = device_codes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_codes is not None:
            result['DeviceCodes'] = self.device_codes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceCodes') is not None:
            self.device_codes = m.get('DeviceCodes')
        return self


class DeleteChannelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        data: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class DeleteChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteChannelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCorpGroupRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        group_id: str = None,
    ):
        self.corp_id = corp_id
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DeleteCorpGroupResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteCorpGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteCorpGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteCorpGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataSourceRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        data_source_id: str = None,
    ):
        self.corp_id = corp_id
        self.data_source_id = data_source_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        return self


class DeleteDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDataSourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDeviceRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        gb_id: str = None,
    ):
        self.corp_id = corp_id
        self.gb_id = gb_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        return self


class DeleteDeviceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDeviceForInstanceRequestDevices(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        region_id: str = None,
    ):
        self.device_id = device_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDeviceForInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        devices: List[DeleteDeviceForInstanceRequestDevices] = None,
        project_id: str = None,
        algorithm_id: str = None,
        delete_instance_flag: bool = None,
        device_count: str = None,
    ):
        self.instance_id = instance_id
        self.devices = devices
        self.project_id = project_id
        self.algorithm_id = algorithm_id
        self.delete_instance_flag = delete_instance_flag
        self.device_count = device_count

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.delete_instance_flag is not None:
            result['DeleteInstanceFlag'] = self.delete_instance_flag
        if self.device_count is not None:
            result['DeviceCount'] = self.device_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = DeleteDeviceForInstanceRequestDevices()
                self.devices.append(temp_model.from_map(k))
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('DeleteInstanceFlag') is not None:
            self.delete_instance_flag = m.get('DeleteInstanceFlag')
        if m.get('DeviceCount') is not None:
            self.device_count = m.get('DeviceCount')
        return self


class DeleteDeviceForInstanceShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        devices_shrink: str = None,
        project_id: str = None,
        algorithm_id: str = None,
        delete_instance_flag: bool = None,
        device_count: str = None,
    ):
        self.instance_id = instance_id
        self.devices_shrink = devices_shrink
        self.project_id = project_id
        self.algorithm_id = algorithm_id
        self.delete_instance_flag = delete_instance_flag
        self.device_count = device_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.devices_shrink is not None:
            result['Devices'] = self.devices_shrink
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.delete_instance_flag is not None:
            result['DeleteInstanceFlag'] = self.delete_instance_flag
        if self.device_count is not None:
            result['DeviceCount'] = self.device_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Devices') is not None:
            self.devices_shrink = m.get('Devices')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('DeleteInstanceFlag') is not None:
            self.delete_instance_flag = m.get('DeleteInstanceFlag')
        if m.get('DeviceCount') is not None:
            self.device_count = m.get('DeviceCount')
        return self


class DeleteDeviceForInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDeviceForInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDeviceForInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDeviceForInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDoubleVerificationGroupRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        double_verification_group_id: str = None,
    ):
        self.id = id
        self.double_verification_group_id = double_verification_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.double_verification_group_id is not None:
            result['DoubleVerificationGroupId'] = self.double_verification_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('DoubleVerificationGroupId') is not None:
            self.double_verification_group_id = m.get('DoubleVerificationGroupId')
        return self


class DeleteDoubleVerificationGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DeleteDoubleVerificationGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDoubleVerificationGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDoubleVerificationGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIPCDeviceRequest(TeaModel):
    def __init__(
        self,
        device_codes: str = None,
    ):
        self.device_codes = device_codes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_codes is not None:
            result['DeviceCodes'] = self.device_codes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceCodes') is not None:
            self.device_codes = m.get('DeviceCodes')
        return self


class DeleteIPCDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        data: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class DeleteIPCDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteIPCDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteIPCDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMarkerRequest(TeaModel):
    def __init__(
        self,
        algorithm_id: str = None,
        sample_id: str = None,
        marker_id: str = None,
    ):
        self.algorithm_id = algorithm_id
        self.sample_id = sample_id
        self.marker_id = marker_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.sample_id is not None:
            result['SampleId'] = self.sample_id
        if self.marker_id is not None:
            result['MarkerId'] = self.marker_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('SampleId') is not None:
            self.sample_id = m.get('SampleId')
        if m.get('MarkerId') is not None:
            self.marker_id = m.get('MarkerId')
        return self


class DeleteMarkerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DeleteMarkerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteMarkerResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteMarkerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNVRDeviceRequest(TeaModel):
    def __init__(
        self,
        device_codes: str = None,
    ):
        self.device_codes = device_codes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_codes is not None:
            result['DeviceCodes'] = self.device_codes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceCodes') is not None:
            self.device_codes = m.get('DeviceCodes')
        return self


class DeleteNVRDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        data: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class DeleteNVRDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteNVRDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteNVRDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProfileRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        isv_sub_id: str = None,
        profile_id: int = None,
    ):
        self.corp_id = corp_id
        self.isv_sub_id = isv_sub_id
        self.profile_id = profile_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.profile_id is not None:
            result['ProfileId'] = self.profile_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('ProfileId') is not None:
            self.profile_id = m.get('ProfileId')
        return self


class DeleteProfileResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: bool = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteProfileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProfileCatalogRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        isv_sub_id: str = None,
        catalog_id: str = None,
    ):
        self.corp_id = corp_id
        self.isv_sub_id = isv_sub_id
        self.catalog_id = catalog_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        return self


class DeleteProfileCatalogResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: bool = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteProfileCatalogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteProfileCatalogResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteProfileCatalogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectRequest(TeaModel):
    def __init__(
        self,
        project_ids: str = None,
    ):
        # 项目id,多个以”,“隔开
        self.project_ids = project_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')
        return self


class DeleteProjectResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteProjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRecordsRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        algorithm_type: str = None,
        attribute_name: str = None,
        operator_type: str = None,
        value: str = None,
    ):
        self.corp_id = corp_id
        self.algorithm_type = algorithm_type
        self.attribute_name = attribute_name
        self.operator_type = operator_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.algorithm_type is not None:
            result['AlgorithmType'] = self.algorithm_type
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('AlgorithmType') is not None:
            self.algorithm_type = m.get('AlgorithmType')
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DeleteRecordsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRecordsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSampleRequest(TeaModel):
    def __init__(
        self,
        algorithm_id: str = None,
        sample_id: str = None,
    ):
        self.algorithm_id = algorithm_id
        self.sample_id = sample_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.sample_id is not None:
            result['SampleId'] = self.sample_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('SampleId') is not None:
            self.sample_id = m.get('SampleId')
        return self


class DeleteSampleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DeleteSampleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSampleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSampleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTrainAlgorithmRequest(TeaModel):
    def __init__(
        self,
        algorithm_id: str = None,
    ):
        self.algorithm_id = algorithm_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        return self


class DeleteTrainAlgorithmResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DeleteTrainAlgorithmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteTrainAlgorithmResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteTrainAlgorithmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTrainLabelRequest(TeaModel):
    def __init__(
        self,
        algorithm_id: str = None,
        label_id: str = None,
    ):
        self.algorithm_id = algorithm_id
        self.label_id = label_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        return self


class DeleteTrainLabelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DeleteTrainLabelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteTrainLabelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteTrainLabelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        isv_sub_id: str = None,
        user_id: int = None,
    ):
        self.corp_id = corp_id
        self.isv_sub_id = isv_sub_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteUserResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: bool = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserGroupRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        isv_sub_id: str = None,
        user_group_id: str = None,
    ):
        self.corp_id = corp_id
        self.isv_sub_id = isv_sub_id
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class DeleteUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: bool = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteUserGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVideoSummaryTaskRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        task_id: str = None,
    ):
        self.corp_id = corp_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteVideoSummaryTaskResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteVideoSummaryTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVideoSummaryTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteVideoSummaryTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAiotDevicesRequest(TeaModel):
    def __init__(
        self,
        corp_id_list: str = None,
        id_list: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.corp_id_list = corp_id_list
        self.id_list = id_list
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id_list is not None:
            result['CorpIdList'] = self.corp_id_list
        if self.id_list is not None:
            result['IdList'] = self.id_list
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpIdList') is not None:
            self.corp_id_list = m.get('CorpIdList')
        if m.get('IdList') is not None:
            self.id_list = m.get('IdList')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAiotDevicesResponseBodyAiotDevicesAiotDeviceList(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        device_id: str = None,
        name: str = None,
        model: str = None,
        ipaddr: str = None,
        ipv6addr: str = None,
        port: int = None,
        longitude: float = None,
        latitude: float = None,
        place_code: str = None,
        place: str = None,
        org_code: str = None,
        cap_direction: str = None,
        monitor_direction: str = None,
        monitor_area_desc: str = None,
        is_online: str = None,
        owner_aps_id: str = None,
        user_id: str = None,
        password: str = None,
        mac: str = None,
        ipv_4netmask: str = None,
        ipv_4gateway: str = None,
        device_type: str = None,
        firmware_version: str = None,
        serial_nuber: str = None,
        manufacturer: str = None,
        id: str = None,
    ):
        self.corp_id = corp_id
        self.device_id = device_id
        self.name = name
        self.model = model
        self.ipaddr = ipaddr
        self.ipv6addr = ipv6addr
        self.port = port
        self.longitude = longitude
        self.latitude = latitude
        self.place_code = place_code
        self.place = place
        self.org_code = org_code
        self.cap_direction = cap_direction
        self.monitor_direction = monitor_direction
        self.monitor_area_desc = monitor_area_desc
        self.is_online = is_online
        self.owner_aps_id = owner_aps_id
        self.user_id = user_id
        self.password = password
        self.mac = mac
        self.ipv_4netmask = ipv_4netmask
        self.ipv_4gateway = ipv_4gateway
        self.device_type = device_type
        self.firmware_version = firmware_version
        self.serial_nuber = serial_nuber
        self.manufacturer = manufacturer
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.name is not None:
            result['Name'] = self.name
        if self.model is not None:
            result['Model'] = self.model
        if self.ipaddr is not None:
            result['IPAddr'] = self.ipaddr
        if self.ipv6addr is not None:
            result['IPV6Addr'] = self.ipv6addr
        if self.port is not None:
            result['Port'] = self.port
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.place_code is not None:
            result['PlaceCode'] = self.place_code
        if self.place is not None:
            result['Place'] = self.place
        if self.org_code is not None:
            result['OrgCode'] = self.org_code
        if self.cap_direction is not None:
            result['CapDirection'] = self.cap_direction
        if self.monitor_direction is not None:
            result['MonitorDirection'] = self.monitor_direction
        if self.monitor_area_desc is not None:
            result['MonitorAreaDesc'] = self.monitor_area_desc
        if self.is_online is not None:
            result['IsOnline'] = self.is_online
        if self.owner_aps_id is not None:
            result['OwnerApsID'] = self.owner_aps_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.password is not None:
            result['Password'] = self.password
        if self.mac is not None:
            result['MAC'] = self.mac
        if self.ipv_4netmask is not None:
            result['IPv4Netmask'] = self.ipv_4netmask
        if self.ipv_4gateway is not None:
            result['IPv4Gateway'] = self.ipv_4gateway
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.firmware_version is not None:
            result['FirmwareVersion'] = self.firmware_version
        if self.serial_nuber is not None:
            result['SerialNuber'] = self.serial_nuber
        if self.manufacturer is not None:
            result['Manufacturer'] = self.manufacturer
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('IPAddr') is not None:
            self.ipaddr = m.get('IPAddr')
        if m.get('IPV6Addr') is not None:
            self.ipv6addr = m.get('IPV6Addr')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('PlaceCode') is not None:
            self.place_code = m.get('PlaceCode')
        if m.get('Place') is not None:
            self.place = m.get('Place')
        if m.get('OrgCode') is not None:
            self.org_code = m.get('OrgCode')
        if m.get('CapDirection') is not None:
            self.cap_direction = m.get('CapDirection')
        if m.get('MonitorDirection') is not None:
            self.monitor_direction = m.get('MonitorDirection')
        if m.get('MonitorAreaDesc') is not None:
            self.monitor_area_desc = m.get('MonitorAreaDesc')
        if m.get('IsOnline') is not None:
            self.is_online = m.get('IsOnline')
        if m.get('OwnerApsID') is not None:
            self.owner_aps_id = m.get('OwnerApsID')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('MAC') is not None:
            self.mac = m.get('MAC')
        if m.get('IPv4Netmask') is not None:
            self.ipv_4netmask = m.get('IPv4Netmask')
        if m.get('IPv4Gateway') is not None:
            self.ipv_4gateway = m.get('IPv4Gateway')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('FirmwareVersion') is not None:
            self.firmware_version = m.get('FirmwareVersion')
        if m.get('SerialNuber') is not None:
            self.serial_nuber = m.get('SerialNuber')
        if m.get('Manufacturer') is not None:
            self.manufacturer = m.get('Manufacturer')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeAiotDevicesResponseBodyAiotDevices(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        aiot_device_list: List[DescribeAiotDevicesResponseBodyAiotDevicesAiotDeviceList] = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.total_num = total_num
        self.aiot_device_list = aiot_device_list

    def validate(self):
        if self.aiot_device_list:
            for k in self.aiot_device_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        result['AiotDeviceList'] = []
        if self.aiot_device_list is not None:
            for k in self.aiot_device_list:
                result['AiotDeviceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        self.aiot_device_list = []
        if m.get('AiotDeviceList') is not None:
            for k in m.get('AiotDeviceList'):
                temp_model = DescribeAiotDevicesResponseBodyAiotDevicesAiotDeviceList()
                self.aiot_device_list.append(temp_model.from_map(k))
        return self


class DescribeAiotDevicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        aiot_devices: DescribeAiotDevicesResponseBodyAiotDevices = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.message = message
        self.code = code
        self.aiot_devices = aiot_devices

    def validate(self):
        if self.aiot_devices:
            self.aiot_devices.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.aiot_devices is not None:
            result['AiotDevices'] = self.aiot_devices.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('AiotDevices') is not None:
            temp_model = DescribeAiotDevicesResponseBodyAiotDevices()
            self.aiot_devices = temp_model.from_map(m['AiotDevices'])
        return self


class DescribeAiotDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAiotDevicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAiotDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAiotPersonTableItemsRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        person_table_item_id: str = None,
        person_table_id: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.id = id
        self.person_table_item_id = person_table_item_id
        self.person_table_id = person_table_id
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.person_table_item_id is not None:
            result['PersonTableItemId'] = self.person_table_item_id
        if self.person_table_id is not None:
            result['PersonTableId'] = self.person_table_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PersonTableItemId') is not None:
            self.person_table_item_id = m.get('PersonTableItemId')
        if m.get('PersonTableId') is not None:
            self.person_table_id = m.get('PersonTableId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAiotPersonTableItemsResponseBodyPersonTableItemsPersonTableItemListIdentificationList(TeaModel):
    def __init__(
        self,
        type: int = None,
        number: str = None,
    ):
        self.type = type
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.number is not None:
            result['Number'] = self.number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        return self


class DescribeAiotPersonTableItemsResponseBodyPersonTableItemsPersonTableItemListImageListFeatureInfo(TeaModel):
    def __init__(
        self,
        vendor: str = None,
        algorithm_version: str = None,
        algorithm_type: str = None,
        table_id: str = None,
        object_id: str = None,
        image_id: str = None,
        feature_data: str = None,
    ):
        self.vendor = vendor
        self.algorithm_version = algorithm_version
        self.algorithm_type = algorithm_type
        self.table_id = table_id
        self.object_id = object_id
        self.image_id = image_id
        self.feature_data = feature_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.algorithm_version is not None:
            result['AlgorithmVersion'] = self.algorithm_version
        if self.algorithm_type is not None:
            result['AlgorithmType'] = self.algorithm_type
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.feature_data is not None:
            result['FeatureData'] = self.feature_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('AlgorithmVersion') is not None:
            self.algorithm_version = m.get('AlgorithmVersion')
        if m.get('AlgorithmType') is not None:
            self.algorithm_type = m.get('AlgorithmType')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('FeatureData') is not None:
            self.feature_data = m.get('FeatureData')
        return self


class DescribeAiotPersonTableItemsResponseBodyPersonTableItemsPersonTableItemListImageList(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        event_sort: str = None,
        device_id: str = None,
        storage_path: str = None,
        size: int = None,
        type: str = None,
        file_format: str = None,
        shot_time: str = None,
        width: int = None,
        height: int = None,
        data: str = None,
        feature_info: DescribeAiotPersonTableItemsResponseBodyPersonTableItemsPersonTableItemListImageListFeatureInfo = None,
    ):
        self.image_id = image_id
        self.event_sort = event_sort
        self.device_id = device_id
        self.storage_path = storage_path
        self.size = size
        self.type = type
        self.file_format = file_format
        self.shot_time = shot_time
        self.width = width
        self.height = height
        self.data = data
        self.feature_info = feature_info

    def validate(self):
        if self.feature_info:
            self.feature_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.event_sort is not None:
            result['EventSort'] = self.event_sort
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.storage_path is not None:
            result['StoragePath'] = self.storage_path
        if self.size is not None:
            result['Size'] = self.size
        if self.type is not None:
            result['Type'] = self.type
        if self.file_format is not None:
            result['FileFormat'] = self.file_format
        if self.shot_time is not None:
            result['ShotTime'] = self.shot_time
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.data is not None:
            result['Data'] = self.data
        if self.feature_info is not None:
            result['FeatureInfo'] = self.feature_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('EventSort') is not None:
            self.event_sort = m.get('EventSort')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('StoragePath') is not None:
            self.storage_path = m.get('StoragePath')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')
        if m.get('ShotTime') is not None:
            self.shot_time = m.get('ShotTime')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('FeatureInfo') is not None:
            temp_model = DescribeAiotPersonTableItemsResponseBodyPersonTableItemsPersonTableItemListImageListFeatureInfo()
            self.feature_info = temp_model.from_map(m['FeatureInfo'])
        return self


class DescribeAiotPersonTableItemsResponseBodyPersonTableItemsPersonTableItemList(TeaModel):
    def __init__(
        self,
        person_table_id: str = None,
        person_id: str = None,
        last_change: str = None,
        person_code: str = None,
        person_name: str = None,
        remarks: str = None,
        identification_num: int = None,
        identification_list: List[DescribeAiotPersonTableItemsResponseBodyPersonTableItemsPersonTableItemListIdentificationList] = None,
        image_num: int = None,
        image_list: List[DescribeAiotPersonTableItemsResponseBodyPersonTableItemsPersonTableItemListImageList] = None,
    ):
        self.person_table_id = person_table_id
        self.person_id = person_id
        self.last_change = last_change
        self.person_code = person_code
        self.person_name = person_name
        self.remarks = remarks
        self.identification_num = identification_num
        self.identification_list = identification_list
        self.image_num = image_num
        self.image_list = image_list

    def validate(self):
        if self.identification_list:
            for k in self.identification_list:
                if k:
                    k.validate()
        if self.image_list:
            for k in self.image_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.person_table_id is not None:
            result['PersonTableId'] = self.person_table_id
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.last_change is not None:
            result['LastChange'] = self.last_change
        if self.person_code is not None:
            result['PersonCode'] = self.person_code
        if self.person_name is not None:
            result['PersonName'] = self.person_name
        if self.remarks is not None:
            result['Remarks'] = self.remarks
        if self.identification_num is not None:
            result['IdentificationNum'] = self.identification_num
        result['IdentificationList'] = []
        if self.identification_list is not None:
            for k in self.identification_list:
                result['IdentificationList'].append(k.to_map() if k else None)
        if self.image_num is not None:
            result['ImageNum'] = self.image_num
        result['ImageList'] = []
        if self.image_list is not None:
            for k in self.image_list:
                result['ImageList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PersonTableId') is not None:
            self.person_table_id = m.get('PersonTableId')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('LastChange') is not None:
            self.last_change = m.get('LastChange')
        if m.get('PersonCode') is not None:
            self.person_code = m.get('PersonCode')
        if m.get('PersonName') is not None:
            self.person_name = m.get('PersonName')
        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')
        if m.get('IdentificationNum') is not None:
            self.identification_num = m.get('IdentificationNum')
        self.identification_list = []
        if m.get('IdentificationList') is not None:
            for k in m.get('IdentificationList'):
                temp_model = DescribeAiotPersonTableItemsResponseBodyPersonTableItemsPersonTableItemListIdentificationList()
                self.identification_list.append(temp_model.from_map(k))
        if m.get('ImageNum') is not None:
            self.image_num = m.get('ImageNum')
        self.image_list = []
        if m.get('ImageList') is not None:
            for k in m.get('ImageList'):
                temp_model = DescribeAiotPersonTableItemsResponseBodyPersonTableItemsPersonTableItemListImageList()
                self.image_list.append(temp_model.from_map(k))
        return self


class DescribeAiotPersonTableItemsResponseBodyPersonTableItems(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        person_table_item_list: List[DescribeAiotPersonTableItemsResponseBodyPersonTableItemsPersonTableItemList] = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.total_num = total_num
        self.person_table_item_list = person_table_item_list

    def validate(self):
        if self.person_table_item_list:
            for k in self.person_table_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        result['PersonTableItemList'] = []
        if self.person_table_item_list is not None:
            for k in self.person_table_item_list:
                result['PersonTableItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        self.person_table_item_list = []
        if m.get('PersonTableItemList') is not None:
            for k in m.get('PersonTableItemList'):
                temp_model = DescribeAiotPersonTableItemsResponseBodyPersonTableItemsPersonTableItemList()
                self.person_table_item_list.append(temp_model.from_map(k))
        return self


class DescribeAiotPersonTableItemsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        person_table_items: DescribeAiotPersonTableItemsResponseBodyPersonTableItems = None,
        message: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.person_table_items = person_table_items
        self.message = message

    def validate(self):
        if self.person_table_items:
            self.person_table_items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.person_table_items is not None:
            result['PersonTableItems'] = self.person_table_items.to_map()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('PersonTableItems') is not None:
            temp_model = DescribeAiotPersonTableItemsResponseBodyPersonTableItems()
            self.person_table_items = temp_model.from_map(m['PersonTableItems'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DescribeAiotPersonTableItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAiotPersonTableItemsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAiotPersonTableItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAiotPersonTablesRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        person_table_id_list: str = None,
    ):
        self.id = id
        self.person_table_id_list = person_table_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.person_table_id_list is not None:
            result['PersonTableIdList'] = self.person_table_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PersonTableIdList') is not None:
            self.person_table_id_list = m.get('PersonTableIdList')
        return self


class DescribeAiotPersonTablesResponseBodyPersonTableList(TeaModel):
    def __init__(
        self,
        person_table_id: str = None,
        name: str = None,
        type: int = None,
        total_person_num: int = None,
        person_num: int = None,
        face_num: int = None,
        last_change: str = None,
        device_id: str = None,
        verification_model_list: List[int] = None,
    ):
        self.person_table_id = person_table_id
        self.name = name
        self.type = type
        self.total_person_num = total_person_num
        self.person_num = person_num
        self.face_num = face_num
        self.last_change = last_change
        self.device_id = device_id
        self.verification_model_list = verification_model_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.person_table_id is not None:
            result['PersonTableId'] = self.person_table_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.total_person_num is not None:
            result['TotalPersonNum'] = self.total_person_num
        if self.person_num is not None:
            result['PersonNum'] = self.person_num
        if self.face_num is not None:
            result['FaceNum'] = self.face_num
        if self.last_change is not None:
            result['LastChange'] = self.last_change
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.verification_model_list is not None:
            result['VerificationModelList'] = self.verification_model_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PersonTableId') is not None:
            self.person_table_id = m.get('PersonTableId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('TotalPersonNum') is not None:
            self.total_person_num = m.get('TotalPersonNum')
        if m.get('PersonNum') is not None:
            self.person_num = m.get('PersonNum')
        if m.get('FaceNum') is not None:
            self.face_num = m.get('FaceNum')
        if m.get('LastChange') is not None:
            self.last_change = m.get('LastChange')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('VerificationModelList') is not None:
            self.verification_model_list = m.get('VerificationModelList')
        return self


class DescribeAiotPersonTablesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        person_table_list: List[DescribeAiotPersonTablesResponseBodyPersonTableList] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.message = message
        self.code = code
        self.person_table_list = person_table_list

    def validate(self):
        if self.person_table_list:
            for k in self.person_table_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        result['PersonTableList'] = []
        if self.person_table_list is not None:
            for k in self.person_table_list:
                result['PersonTableList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.person_table_list = []
        if m.get('PersonTableList') is not None:
            for k in m.get('PersonTableList'):
                temp_model = DescribeAiotPersonTablesResponseBodyPersonTableList()
                self.person_table_list.append(temp_model.from_map(k))
        return self


class DescribeAiotPersonTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAiotPersonTablesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAiotPersonTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDevicesRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        corp_id_list: str = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.corp_id_list = corp_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.corp_id_list is not None:
            result['CorpIdList'] = self.corp_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CorpIdList') is not None:
            self.corp_id_list = m.get('CorpIdList')
        return self


class DescribeDevicesResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        status: str = None,
        device_name: str = None,
        device_type: str = None,
        device_id: str = None,
        device_address: str = None,
        create_time: str = None,
        corp_id: str = None,
        longitude: str = None,
        in_protocol: str = None,
        latitude: str = None,
        vendor: str = None,
        captured_picture_id: str = None,
    ):
        self.status = status
        self.device_name = device_name
        self.device_type = device_type
        self.device_id = device_id
        self.device_address = device_address
        self.create_time = create_time
        self.corp_id = corp_id
        self.longitude = longitude
        self.in_protocol = in_protocol
        self.latitude = latitude
        self.vendor = vendor
        self.captured_picture_id = captured_picture_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_address is not None:
            result['DeviceAddress'] = self.device_address
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.in_protocol is not None:
            result['InProtocol'] = self.in_protocol
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.captured_picture_id is not None:
            result['CapturedPictureId'] = self.captured_picture_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceAddress') is not None:
            self.device_address = m.get('DeviceAddress')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('InProtocol') is not None:
            self.in_protocol = m.get('InProtocol')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('CapturedPictureId') is not None:
            self.captured_picture_id = m.get('CapturedPictureId')
        return self


class DescribeDevicesResponseBodyData(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        records: List[DescribeDevicesResponseBodyDataRecords] = None,
        total_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_num = page_num
        self.records = records
        self.total_page = total_page
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeDevicesResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDevicesResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: DescribeDevicesResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeDevicesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDevicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribesDoubleVerificationGroupsRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        double_verification_group_ids: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.id = id
        self.double_verification_group_ids = double_verification_group_ids
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.double_verification_group_ids is not None:
            result['DoubleVerificationGroupIds'] = self.double_verification_group_ids
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('DoubleVerificationGroupIds') is not None:
            self.double_verification_group_ids = m.get('DoubleVerificationGroupIds')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribesDoubleVerificationGroupsResponseBodyDoubleVerificationGroupsDoubleVerificationGroupListPersonIdList(TeaModel):
    def __init__(
        self,
        person_table_id: str = None,
        person_id: str = None,
    ):
        self.person_table_id = person_table_id
        self.person_id = person_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.person_table_id is not None:
            result['PersonTableId'] = self.person_table_id
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PersonTableId') is not None:
            self.person_table_id = m.get('PersonTableId')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        return self


class DescribesDoubleVerificationGroupsResponseBodyDoubleVerificationGroupsDoubleVerificationGroupList(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        interval: int = None,
        last_change: str = None,
        member_number: int = None,
        person_id_list: List[DescribesDoubleVerificationGroupsResponseBodyDoubleVerificationGroupsDoubleVerificationGroupListPersonIdList] = None,
        enabled: str = None,
        device_id: str = None,
    ):
        self.group_id = group_id
        self.interval = interval
        self.last_change = last_change
        self.member_number = member_number
        self.person_id_list = person_id_list
        self.enabled = enabled
        self.device_id = device_id

    def validate(self):
        if self.person_id_list:
            for k in self.person_id_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.last_change is not None:
            result['LastChange'] = self.last_change
        if self.member_number is not None:
            result['MemberNumber'] = self.member_number
        result['PersonIdList'] = []
        if self.person_id_list is not None:
            for k in self.person_id_list:
                result['PersonIdList'].append(k.to_map() if k else None)
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('LastChange') is not None:
            self.last_change = m.get('LastChange')
        if m.get('MemberNumber') is not None:
            self.member_number = m.get('MemberNumber')
        self.person_id_list = []
        if m.get('PersonIdList') is not None:
            for k in m.get('PersonIdList'):
                temp_model = DescribesDoubleVerificationGroupsResponseBodyDoubleVerificationGroupsDoubleVerificationGroupListPersonIdList()
                self.person_id_list.append(temp_model.from_map(k))
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class DescribesDoubleVerificationGroupsResponseBodyDoubleVerificationGroups(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        double_verification_group_list: List[DescribesDoubleVerificationGroupsResponseBodyDoubleVerificationGroupsDoubleVerificationGroupList] = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.total_num = total_num
        self.double_verification_group_list = double_verification_group_list

    def validate(self):
        if self.double_verification_group_list:
            for k in self.double_verification_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        result['DoubleVerificationGroupList'] = []
        if self.double_verification_group_list is not None:
            for k in self.double_verification_group_list:
                result['DoubleVerificationGroupList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        self.double_verification_group_list = []
        if m.get('DoubleVerificationGroupList') is not None:
            for k in m.get('DoubleVerificationGroupList'):
                temp_model = DescribesDoubleVerificationGroupsResponseBodyDoubleVerificationGroupsDoubleVerificationGroupList()
                self.double_verification_group_list.append(temp_model.from_map(k))
        return self


class DescribesDoubleVerificationGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        double_verification_groups: DescribesDoubleVerificationGroupsResponseBodyDoubleVerificationGroups = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message
        self.double_verification_groups = double_verification_groups

    def validate(self):
        if self.double_verification_groups:
            self.double_verification_groups.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.double_verification_groups is not None:
            result['DoubleVerificationGroups'] = self.double_verification_groups.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DoubleVerificationGroups') is not None:
            temp_model = DescribesDoubleVerificationGroupsResponseBodyDoubleVerificationGroups()
            self.double_verification_groups = temp_model.from_map(m['DoubleVerificationGroups'])
        return self


class DescribesDoubleVerificationGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribesDoubleVerificationGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribesDoubleVerificationGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAiotStorageInfoRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
    ):
        self.corp_id = corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        return self


class GetAiotStorageInfoResponseBodyEventAlarmMq(TeaModel):
    def __init__(
        self,
        mq_type: str = None,
        alarm_topic: str = None,
        event_topic: str = None,
        instance_id: str = None,
        domain: str = None,
        version: str = None,
        region_id: str = None,
        brokers: List[str] = None,
    ):
        self.mq_type = mq_type
        self.alarm_topic = alarm_topic
        self.event_topic = event_topic
        self.instance_id = instance_id
        self.domain = domain
        self.version = version
        self.region_id = region_id
        self.brokers = brokers

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mq_type is not None:
            result['MqType'] = self.mq_type
        if self.alarm_topic is not None:
            result['AlarmTopic'] = self.alarm_topic
        if self.event_topic is not None:
            result['EventTopic'] = self.event_topic
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.version is not None:
            result['Version'] = self.version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.brokers is not None:
            result['Brokers'] = self.brokers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MqType') is not None:
            self.mq_type = m.get('MqType')
        if m.get('AlarmTopic') is not None:
            self.alarm_topic = m.get('AlarmTopic')
        if m.get('EventTopic') is not None:
            self.event_topic = m.get('EventTopic')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Brokers') is not None:
            self.brokers = m.get('Brokers')
        return self


class GetAiotStorageInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        event_alarm_mq: GetAiotStorageInfoResponseBodyEventAlarmMq = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message
        self.event_alarm_mq = event_alarm_mq

    def validate(self):
        if self.event_alarm_mq:
            self.event_alarm_mq.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.event_alarm_mq is not None:
            result['EventAlarmMq'] = self.event_alarm_mq.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('EventAlarmMq') is not None:
            temp_model = GetAiotStorageInfoResponseBodyEventAlarmMq()
            self.event_alarm_mq = temp_model.from_map(m['EventAlarmMq'])
        return self


class GetAiotStorageInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAiotStorageInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAiotStorageInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBodyOptionsRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
    ):
        self.corp_id = corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        return self


class GetBodyOptionsResponseBodyDataOptionList(TeaModel):
    def __init__(
        self,
        key: str = None,
        name: str = None,
    ):
        self.key = key
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetBodyOptionsResponseBodyData(TeaModel):
    def __init__(
        self,
        key: str = None,
        option_list: List[GetBodyOptionsResponseBodyDataOptionList] = None,
        name: str = None,
    ):
        self.key = key
        self.option_list = option_list
        self.name = name

    def validate(self):
        if self.option_list:
            for k in self.option_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        result['OptionList'] = []
        if self.option_list is not None:
            for k in self.option_list:
                result['OptionList'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        self.option_list = []
        if m.get('OptionList') is not None:
            for k in m.get('OptionList'):
                temp_model = GetBodyOptionsResponseBodyDataOptionList()
                self.option_list.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetBodyOptionsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[GetBodyOptionsResponseBodyData] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetBodyOptionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetBodyOptionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetBodyOptionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetBodyOptionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCatalogListRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        isv_sub_id: str = None,
    ):
        self.corp_id = corp_id
        self.isv_sub_id = isv_sub_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        return self


class GetCatalogListResponseBodyData(TeaModel):
    def __init__(
        self,
        catalog_id: int = None,
        catalog_name: str = None,
        isv_sub_id: str = None,
        parent_catalog_id: int = None,
        profile_count: int = None,
    ):
        self.catalog_id = catalog_id
        self.catalog_name = catalog_name
        self.isv_sub_id = isv_sub_id
        self.parent_catalog_id = parent_catalog_id
        self.profile_count = profile_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.parent_catalog_id is not None:
            result['ParentCatalogId'] = self.parent_catalog_id
        if self.profile_count is not None:
            result['ProfileCount'] = self.profile_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('ParentCatalogId') is not None:
            self.parent_catalog_id = m.get('ParentCatalogId')
        if m.get('ProfileCount') is not None:
            self.profile_count = m.get('ProfileCount')
        return self


class GetCatalogListResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[GetCatalogListResponseBodyData] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetCatalogListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetCatalogListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCatalogListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetCatalogListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCityCodeResponseBodyData(TeaModel):
    def __init__(
        self,
        city_address: str = None,
        city_code: str = None,
    ):
        self.city_address = city_address
        self.city_code = city_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city_address is not None:
            result['CityAddress'] = self.city_address
        if self.city_code is not None:
            result['CityCode'] = self.city_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityAddress') is not None:
            self.city_address = m.get('CityAddress')
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')
        return self


class GetCityCodeResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        code: str = None,
        data: List[GetCityCodeResponseBodyData] = None,
        request_id: str = None,
    ):
        self.message = message
        self.code = code
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetCityCodeResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCityCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCityCodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetCityCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceCaptureStrategyRequest(TeaModel):
    def __init__(
        self,
        device_code: str = None,
        device_type: str = None,
    ):
        # 设备通道号
        self.device_code = device_code
        # 设备类型
        self.device_type = device_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_code is not None:
            result['DeviceCode'] = self.device_code
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceCode') is not None:
            self.device_code = m.get('DeviceCode')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        return self


class GetDeviceCaptureStrategyResponseBodyData(TeaModel):
    def __init__(
        self,
        device_type: str = None,
        device_code: str = None,
        monday_capture_strategy: str = None,
        tuesday_capture_strategy: str = None,
        wednesday_capture_strategy: str = None,
        thursday_capture_strategy: str = None,
        friday_capture_strategy: str = None,
        saturday_capture_strategy: str = None,
        sunday_capture_strategy: str = None,
    ):
        # 设备类型
        self.device_type = device_type
        # 设备通道
        self.device_code = device_code
        # 星期一抓取策略
        self.monday_capture_strategy = monday_capture_strategy
        # 星期二抓取策略
        self.tuesday_capture_strategy = tuesday_capture_strategy
        # 星期三抓取策略
        self.wednesday_capture_strategy = wednesday_capture_strategy
        # 星期四抓取策略
        self.thursday_capture_strategy = thursday_capture_strategy
        # 星期五抓取策略
        self.friday_capture_strategy = friday_capture_strategy
        # 星期六抓取策略
        self.saturday_capture_strategy = saturday_capture_strategy
        # 星期日抓取策略
        self.sunday_capture_strategy = sunday_capture_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.device_code is not None:
            result['DeviceCode'] = self.device_code
        if self.monday_capture_strategy is not None:
            result['MondayCaptureStrategy'] = self.monday_capture_strategy
        if self.tuesday_capture_strategy is not None:
            result['TuesdayCaptureStrategy'] = self.tuesday_capture_strategy
        if self.wednesday_capture_strategy is not None:
            result['WednesdayCaptureStrategy'] = self.wednesday_capture_strategy
        if self.thursday_capture_strategy is not None:
            result['ThursdayCaptureStrategy'] = self.thursday_capture_strategy
        if self.friday_capture_strategy is not None:
            result['FridayCaptureStrategy'] = self.friday_capture_strategy
        if self.saturday_capture_strategy is not None:
            result['SaturdayCaptureStrategy'] = self.saturday_capture_strategy
        if self.sunday_capture_strategy is not None:
            result['SundayCaptureStrategy'] = self.sunday_capture_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('DeviceCode') is not None:
            self.device_code = m.get('DeviceCode')
        if m.get('MondayCaptureStrategy') is not None:
            self.monday_capture_strategy = m.get('MondayCaptureStrategy')
        if m.get('TuesdayCaptureStrategy') is not None:
            self.tuesday_capture_strategy = m.get('TuesdayCaptureStrategy')
        if m.get('WednesdayCaptureStrategy') is not None:
            self.wednesday_capture_strategy = m.get('WednesdayCaptureStrategy')
        if m.get('ThursdayCaptureStrategy') is not None:
            self.thursday_capture_strategy = m.get('ThursdayCaptureStrategy')
        if m.get('FridayCaptureStrategy') is not None:
            self.friday_capture_strategy = m.get('FridayCaptureStrategy')
        if m.get('SaturdayCaptureStrategy') is not None:
            self.saturday_capture_strategy = m.get('SaturdayCaptureStrategy')
        if m.get('SundayCaptureStrategy') is not None:
            self.sunday_capture_strategy = m.get('SundayCaptureStrategy')
        return self


class GetDeviceCaptureStrategyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: GetDeviceCaptureStrategyResponseBodyData = None,
        request_id: str = None,
    ):
        # 错误码
        self.code = code
        # 错误信息
        self.message = message
        # 响应数据内容
        self.data = data
        # RequestId
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = GetDeviceCaptureStrategyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDeviceCaptureStrategyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDeviceCaptureStrategyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDeviceCaptureStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceConfigRequest(TeaModel):
    def __init__(
        self,
        device_sn: str = None,
        device_time_stamp: str = None,
    ):
        self.device_sn = device_sn
        self.device_time_stamp = device_time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.device_time_stamp is not None:
            result['DeviceTimeStamp'] = self.device_time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('DeviceTimeStamp') is not None:
            self.device_time_stamp = m.get('DeviceTimeStamp')
        return self


class GetDeviceConfigResponseBodyOSDList(TeaModel):
    def __init__(
        self,
        left_top_x: str = None,
        left_top_y: str = None,
        text: str = None,
    ):
        self.left_top_x = left_top_x
        self.left_top_y = left_top_y
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left_top_x is not None:
            result['LeftTopX'] = self.left_top_x
        if self.left_top_y is not None:
            result['LeftTopY'] = self.left_top_y
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LeftTopX') is not None:
            self.left_top_x = m.get('LeftTopX')
        if m.get('LeftTopY') is not None:
            self.left_top_y = m.get('LeftTopY')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetDeviceConfigResponseBodyChannelList(TeaModel):
    def __init__(
        self,
        channel_gb_id: str = None,
        monday_capture_strategy: str = None,
        tuesday_capture_strategy: str = None,
        wednesday_capture_strategy: str = None,
        thursday_capture_strategy: str = None,
        friday_capture_strategy: str = None,
        saturday_capture_strategy: str = None,
        sunday_capture_strategy: str = None,
    ):
        self.channel_gb_id = channel_gb_id
        self.monday_capture_strategy = monday_capture_strategy
        self.tuesday_capture_strategy = tuesday_capture_strategy
        self.wednesday_capture_strategy = wednesday_capture_strategy
        self.thursday_capture_strategy = thursday_capture_strategy
        self.friday_capture_strategy = friday_capture_strategy
        self.saturday_capture_strategy = saturday_capture_strategy
        self.sunday_capture_strategy = sunday_capture_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_gb_id is not None:
            result['ChannelGbId'] = self.channel_gb_id
        if self.monday_capture_strategy is not None:
            result['MondayCaptureStrategy'] = self.monday_capture_strategy
        if self.tuesday_capture_strategy is not None:
            result['TuesdayCaptureStrategy'] = self.tuesday_capture_strategy
        if self.wednesday_capture_strategy is not None:
            result['WednesdayCaptureStrategy'] = self.wednesday_capture_strategy
        if self.thursday_capture_strategy is not None:
            result['ThursdayCaptureStrategy'] = self.thursday_capture_strategy
        if self.friday_capture_strategy is not None:
            result['FridayCaptureStrategy'] = self.friday_capture_strategy
        if self.saturday_capture_strategy is not None:
            result['SaturdayCaptureStrategy'] = self.saturday_capture_strategy
        if self.sunday_capture_strategy is not None:
            result['SundayCaptureStrategy'] = self.sunday_capture_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelGbId') is not None:
            self.channel_gb_id = m.get('ChannelGbId')
        if m.get('MondayCaptureStrategy') is not None:
            self.monday_capture_strategy = m.get('MondayCaptureStrategy')
        if m.get('TuesdayCaptureStrategy') is not None:
            self.tuesday_capture_strategy = m.get('TuesdayCaptureStrategy')
        if m.get('WednesdayCaptureStrategy') is not None:
            self.wednesday_capture_strategy = m.get('WednesdayCaptureStrategy')
        if m.get('ThursdayCaptureStrategy') is not None:
            self.thursday_capture_strategy = m.get('ThursdayCaptureStrategy')
        if m.get('FridayCaptureStrategy') is not None:
            self.friday_capture_strategy = m.get('FridayCaptureStrategy')
        if m.get('SaturdayCaptureStrategy') is not None:
            self.saturday_capture_strategy = m.get('SaturdayCaptureStrategy')
        if m.get('SundayCaptureStrategy') is not None:
            self.sunday_capture_strategy = m.get('SundayCaptureStrategy')
        return self


class GetDeviceConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        retry_interval: str = None,
        code: str = None,
        audio_enable: str = None,
        audio_format: str = None,
        bit_rate: str = None,
        device_address: str = None,
        device_name: str = None,
        encode_format: str = None,
        frame_rate: str = None,
        gov_length: int = None,
        latitude: str = None,
        longitude: str = None,
        osdlist: List[GetDeviceConfigResponseBodyOSDList] = None,
        osdtime_enable: str = None,
        osdtime_type: str = None,
        osdtime_x: str = None,
        osdtime_y: str = None,
        resolution: str = None,
        device_id: str = None,
        user_name: str = None,
        pass_word: str = None,
        protocol: str = None,
        server_id: str = None,
        server_port: str = None,
        server_ip: str = None,
        channel_list: List[GetDeviceConfigResponseBodyChannelList] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.message = message
        self.retry_interval = retry_interval
        self.code = code
        self.audio_enable = audio_enable
        self.audio_format = audio_format
        self.bit_rate = bit_rate
        self.device_address = device_address
        self.device_name = device_name
        self.encode_format = encode_format
        self.frame_rate = frame_rate
        self.gov_length = gov_length
        self.latitude = latitude
        self.longitude = longitude
        self.osdlist = osdlist
        self.osdtime_enable = osdtime_enable
        self.osdtime_type = osdtime_type
        self.osdtime_x = osdtime_x
        self.osdtime_y = osdtime_y
        self.resolution = resolution
        self.device_id = device_id
        self.user_name = user_name
        self.pass_word = pass_word
        self.protocol = protocol
        self.server_id = server_id
        self.server_port = server_port
        self.server_ip = server_ip
        self.channel_list = channel_list

    def validate(self):
        if self.osdlist:
            for k in self.osdlist:
                if k:
                    k.validate()
        if self.channel_list:
            for k in self.channel_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.retry_interval is not None:
            result['RetryInterval'] = self.retry_interval
        if self.code is not None:
            result['Code'] = self.code
        if self.audio_enable is not None:
            result['AudioEnable'] = self.audio_enable
        if self.audio_format is not None:
            result['AudioFormat'] = self.audio_format
        if self.bit_rate is not None:
            result['BitRate'] = self.bit_rate
        if self.device_address is not None:
            result['DeviceAddress'] = self.device_address
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.encode_format is not None:
            result['EncodeFormat'] = self.encode_format
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.gov_length is not None:
            result['GovLength'] = self.gov_length
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        result['OSDList'] = []
        if self.osdlist is not None:
            for k in self.osdlist:
                result['OSDList'].append(k.to_map() if k else None)
        if self.osdtime_enable is not None:
            result['OSDTimeEnable'] = self.osdtime_enable
        if self.osdtime_type is not None:
            result['OSDTimeType'] = self.osdtime_type
        if self.osdtime_x is not None:
            result['OSDTimeX'] = self.osdtime_x
        if self.osdtime_y is not None:
            result['OSDTimeY'] = self.osdtime_y
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.pass_word is not None:
            result['PassWord'] = self.pass_word
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.server_port is not None:
            result['ServerPort'] = self.server_port
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        result['ChannelList'] = []
        if self.channel_list is not None:
            for k in self.channel_list:
                result['ChannelList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RetryInterval') is not None:
            self.retry_interval = m.get('RetryInterval')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('AudioEnable') is not None:
            self.audio_enable = m.get('AudioEnable')
        if m.get('AudioFormat') is not None:
            self.audio_format = m.get('AudioFormat')
        if m.get('BitRate') is not None:
            self.bit_rate = m.get('BitRate')
        if m.get('DeviceAddress') is not None:
            self.device_address = m.get('DeviceAddress')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EncodeFormat') is not None:
            self.encode_format = m.get('EncodeFormat')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('GovLength') is not None:
            self.gov_length = m.get('GovLength')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        self.osdlist = []
        if m.get('OSDList') is not None:
            for k in m.get('OSDList'):
                temp_model = GetDeviceConfigResponseBodyOSDList()
                self.osdlist.append(temp_model.from_map(k))
        if m.get('OSDTimeEnable') is not None:
            self.osdtime_enable = m.get('OSDTimeEnable')
        if m.get('OSDTimeType') is not None:
            self.osdtime_type = m.get('OSDTimeType')
        if m.get('OSDTimeX') is not None:
            self.osdtime_x = m.get('OSDTimeX')
        if m.get('OSDTimeY') is not None:
            self.osdtime_y = m.get('OSDTimeY')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('PassWord') is not None:
            self.pass_word = m.get('PassWord')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('ServerPort') is not None:
            self.server_port = m.get('ServerPort')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        self.channel_list = []
        if m.get('ChannelList') is not None:
            for k in m.get('ChannelList'):
                temp_model = GetDeviceConfigResponseBodyChannelList()
                self.channel_list.append(temp_model.from_map(k))
        return self


class GetDeviceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDeviceConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDeviceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceLiveUrlRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        stream_type: int = None,
        out_protocol: str = None,
        corp_id: str = None,
        gb_id: str = None,
    ):
        self.device_id = device_id
        self.stream_type = stream_type
        self.out_protocol = out_protocol
        self.corp_id = corp_id
        self.gb_id = gb_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        return self


class GetDeviceLiveUrlResponseBody(TeaModel):
    def __init__(
        self,
        stream_type: int = None,
        request_id: str = None,
        message: str = None,
        code: str = None,
        out_protocol: str = None,
        url: str = None,
    ):
        self.stream_type = stream_type
        self.request_id = request_id
        self.message = message
        self.code = code
        self.out_protocol = out_protocol
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetDeviceLiveUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDeviceLiveUrlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDeviceLiveUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDevicePictureRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
    ):
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class GetDevicePictureResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetDevicePictureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDevicePictureResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDevicePictureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceVideoUrlRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        gb_id: str = None,
        start_time: int = None,
        end_time: int = None,
        device_id: str = None,
        out_protocol: str = None,
    ):
        self.corp_id = corp_id
        self.gb_id = gb_id
        self.start_time = start_time
        self.end_time = end_time
        self.device_id = device_id
        self.out_protocol = out_protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')
        return self


class GetDeviceVideoUrlResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        out_protocol: str = None,
        url: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.out_protocol = out_protocol
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetDeviceVideoUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDeviceVideoUrlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDeviceVideoUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFaceModelResultRequest(TeaModel):
    def __init__(
        self,
        picture_id: str = None,
        picture_content: str = None,
        picture_url: str = None,
    ):
        self.picture_id = picture_id
        self.picture_content = picture_content
        self.picture_url = picture_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.picture_id is not None:
            result['PictureId'] = self.picture_id
        if self.picture_content is not None:
            result['PictureContent'] = self.picture_content
        if self.picture_url is not None:
            result['PictureUrl'] = self.picture_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PictureId') is not None:
            self.picture_id = m.get('PictureId')
        if m.get('PictureContent') is not None:
            self.picture_content = m.get('PictureContent')
        if m.get('PictureUrl') is not None:
            self.picture_url = m.get('PictureUrl')
        return self


class GetFaceModelResultResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        right_bottom_y: float = None,
        hair_color_reliability: str = None,
        hair_color: int = None,
        face_style: str = None,
        glass_style_reliability: str = None,
        mustache_style_reliability: str = None,
        respirator_color_reliability: str = None,
        right_bottom_x: float = None,
        age_up_limit: int = None,
        age_up_limit_reliability: str = None,
        hair_style: int = None,
        age_lower_limit: int = None,
        left_top_y: float = None,
        feature_data: List[float] = None,
        skin_color_reliability: str = None,
        cap_color: int = None,
        face_style_reliability: str = None,
        cap_style_reliability: str = None,
        gender_code_reliability: str = None,
        hair_style_reliability: str = None,
        glass_color_reliability: str = None,
        ethic_code: int = None,
        respirator_color: int = None,
        mustache_style: str = None,
        glass_color: int = None,
        glass_style: int = None,
        skin_color: int = None,
        cap_color_reliability: str = None,
        cap_style: int = None,
        gender_code: int = None,
        left_top_x: float = None,
        age_lower_limit_reliability: str = None,
        ethic_code_reliability: str = None,
    ):
        self.right_bottom_y = right_bottom_y
        self.hair_color_reliability = hair_color_reliability
        self.hair_color = hair_color
        self.face_style = face_style
        self.glass_style_reliability = glass_style_reliability
        self.mustache_style_reliability = mustache_style_reliability
        self.respirator_color_reliability = respirator_color_reliability
        self.right_bottom_x = right_bottom_x
        self.age_up_limit = age_up_limit
        self.age_up_limit_reliability = age_up_limit_reliability
        self.hair_style = hair_style
        self.age_lower_limit = age_lower_limit
        self.left_top_y = left_top_y
        self.feature_data = feature_data
        self.skin_color_reliability = skin_color_reliability
        self.cap_color = cap_color
        self.face_style_reliability = face_style_reliability
        self.cap_style_reliability = cap_style_reliability
        self.gender_code_reliability = gender_code_reliability
        self.hair_style_reliability = hair_style_reliability
        self.glass_color_reliability = glass_color_reliability
        self.ethic_code = ethic_code
        self.respirator_color = respirator_color
        self.mustache_style = mustache_style
        self.glass_color = glass_color
        self.glass_style = glass_style
        self.skin_color = skin_color
        self.cap_color_reliability = cap_color_reliability
        self.cap_style = cap_style
        self.gender_code = gender_code
        self.left_top_x = left_top_x
        self.age_lower_limit_reliability = age_lower_limit_reliability
        self.ethic_code_reliability = ethic_code_reliability

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.right_bottom_y is not None:
            result['RightBottomY'] = self.right_bottom_y
        if self.hair_color_reliability is not None:
            result['HairColorReliability'] = self.hair_color_reliability
        if self.hair_color is not None:
            result['HairColor'] = self.hair_color
        if self.face_style is not None:
            result['FaceStyle'] = self.face_style
        if self.glass_style_reliability is not None:
            result['GlassStyleReliability'] = self.glass_style_reliability
        if self.mustache_style_reliability is not None:
            result['MustacheStyleReliability'] = self.mustache_style_reliability
        if self.respirator_color_reliability is not None:
            result['RespiratorColorReliability'] = self.respirator_color_reliability
        if self.right_bottom_x is not None:
            result['RightBottomX'] = self.right_bottom_x
        if self.age_up_limit is not None:
            result['AgeUpLimit'] = self.age_up_limit
        if self.age_up_limit_reliability is not None:
            result['AgeUpLimitReliability'] = self.age_up_limit_reliability
        if self.hair_style is not None:
            result['HairStyle'] = self.hair_style
        if self.age_lower_limit is not None:
            result['AgeLowerLimit'] = self.age_lower_limit
        if self.left_top_y is not None:
            result['LeftTopY'] = self.left_top_y
        if self.feature_data is not None:
            result['FeatureData'] = self.feature_data
        if self.skin_color_reliability is not None:
            result['SkinColorReliability'] = self.skin_color_reliability
        if self.cap_color is not None:
            result['CapColor'] = self.cap_color
        if self.face_style_reliability is not None:
            result['FaceStyleReliability'] = self.face_style_reliability
        if self.cap_style_reliability is not None:
            result['CapStyleReliability'] = self.cap_style_reliability
        if self.gender_code_reliability is not None:
            result['GenderCodeReliability'] = self.gender_code_reliability
        if self.hair_style_reliability is not None:
            result['HairStyleReliability'] = self.hair_style_reliability
        if self.glass_color_reliability is not None:
            result['GlassColorReliability'] = self.glass_color_reliability
        if self.ethic_code is not None:
            result['EthicCode'] = self.ethic_code
        if self.respirator_color is not None:
            result['RespiratorColor'] = self.respirator_color
        if self.mustache_style is not None:
            result['MustacheStyle'] = self.mustache_style
        if self.glass_color is not None:
            result['GlassColor'] = self.glass_color
        if self.glass_style is not None:
            result['GlassStyle'] = self.glass_style
        if self.skin_color is not None:
            result['SkinColor'] = self.skin_color
        if self.cap_color_reliability is not None:
            result['CapColorReliability'] = self.cap_color_reliability
        if self.cap_style is not None:
            result['CapStyle'] = self.cap_style
        if self.gender_code is not None:
            result['GenderCode'] = self.gender_code
        if self.left_top_x is not None:
            result['LeftTopX'] = self.left_top_x
        if self.age_lower_limit_reliability is not None:
            result['AgeLowerLimitReliability'] = self.age_lower_limit_reliability
        if self.ethic_code_reliability is not None:
            result['EthicCodeReliability'] = self.ethic_code_reliability
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RightBottomY') is not None:
            self.right_bottom_y = m.get('RightBottomY')
        if m.get('HairColorReliability') is not None:
            self.hair_color_reliability = m.get('HairColorReliability')
        if m.get('HairColor') is not None:
            self.hair_color = m.get('HairColor')
        if m.get('FaceStyle') is not None:
            self.face_style = m.get('FaceStyle')
        if m.get('GlassStyleReliability') is not None:
            self.glass_style_reliability = m.get('GlassStyleReliability')
        if m.get('MustacheStyleReliability') is not None:
            self.mustache_style_reliability = m.get('MustacheStyleReliability')
        if m.get('RespiratorColorReliability') is not None:
            self.respirator_color_reliability = m.get('RespiratorColorReliability')
        if m.get('RightBottomX') is not None:
            self.right_bottom_x = m.get('RightBottomX')
        if m.get('AgeUpLimit') is not None:
            self.age_up_limit = m.get('AgeUpLimit')
        if m.get('AgeUpLimitReliability') is not None:
            self.age_up_limit_reliability = m.get('AgeUpLimitReliability')
        if m.get('HairStyle') is not None:
            self.hair_style = m.get('HairStyle')
        if m.get('AgeLowerLimit') is not None:
            self.age_lower_limit = m.get('AgeLowerLimit')
        if m.get('LeftTopY') is not None:
            self.left_top_y = m.get('LeftTopY')
        if m.get('FeatureData') is not None:
            self.feature_data = m.get('FeatureData')
        if m.get('SkinColorReliability') is not None:
            self.skin_color_reliability = m.get('SkinColorReliability')
        if m.get('CapColor') is not None:
            self.cap_color = m.get('CapColor')
        if m.get('FaceStyleReliability') is not None:
            self.face_style_reliability = m.get('FaceStyleReliability')
        if m.get('CapStyleReliability') is not None:
            self.cap_style_reliability = m.get('CapStyleReliability')
        if m.get('GenderCodeReliability') is not None:
            self.gender_code_reliability = m.get('GenderCodeReliability')
        if m.get('HairStyleReliability') is not None:
            self.hair_style_reliability = m.get('HairStyleReliability')
        if m.get('GlassColorReliability') is not None:
            self.glass_color_reliability = m.get('GlassColorReliability')
        if m.get('EthicCode') is not None:
            self.ethic_code = m.get('EthicCode')
        if m.get('RespiratorColor') is not None:
            self.respirator_color = m.get('RespiratorColor')
        if m.get('MustacheStyle') is not None:
            self.mustache_style = m.get('MustacheStyle')
        if m.get('GlassColor') is not None:
            self.glass_color = m.get('GlassColor')
        if m.get('GlassStyle') is not None:
            self.glass_style = m.get('GlassStyle')
        if m.get('SkinColor') is not None:
            self.skin_color = m.get('SkinColor')
        if m.get('CapColorReliability') is not None:
            self.cap_color_reliability = m.get('CapColorReliability')
        if m.get('CapStyle') is not None:
            self.cap_style = m.get('CapStyle')
        if m.get('GenderCode') is not None:
            self.gender_code = m.get('GenderCode')
        if m.get('LeftTopX') is not None:
            self.left_top_x = m.get('LeftTopX')
        if m.get('AgeLowerLimitReliability') is not None:
            self.age_lower_limit_reliability = m.get('AgeLowerLimitReliability')
        if m.get('EthicCodeReliability') is not None:
            self.ethic_code_reliability = m.get('EthicCodeReliability')
        return self


class GetFaceModelResultResponseBodyData(TeaModel):
    def __init__(
        self,
        records: List[GetFaceModelResultResponseBodyDataRecords] = None,
    ):
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = GetFaceModelResultResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        return self


class GetFaceModelResultResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetFaceModelResultResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetFaceModelResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetFaceModelResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetFaceModelResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetFaceModelResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFaceOptionsRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
    ):
        self.corp_id = corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        return self


class GetFaceOptionsResponseBodyDataOptionList(TeaModel):
    def __init__(
        self,
        key: str = None,
        name: str = None,
    ):
        self.key = key
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetFaceOptionsResponseBodyData(TeaModel):
    def __init__(
        self,
        key: str = None,
        option_list: List[GetFaceOptionsResponseBodyDataOptionList] = None,
        name: str = None,
    ):
        self.key = key
        self.option_list = option_list
        self.name = name

    def validate(self):
        if self.option_list:
            for k in self.option_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        result['OptionList'] = []
        if self.option_list is not None:
            for k in self.option_list:
                result['OptionList'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        self.option_list = []
        if m.get('OptionList') is not None:
            for k in m.get('OptionList'):
                temp_model = GetFaceOptionsResponseBodyDataOptionList()
                self.option_list.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetFaceOptionsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[GetFaceOptionsResponseBodyData] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetFaceOptionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetFaceOptionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetFaceOptionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetFaceOptionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInventoryRequest(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
    ):
        self.commodity_code = commodity_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        return self


class GetInventoryResponseBodyDataResultObject(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        current_inventory: str = None,
        inventory_id: str = None,
        instance_id: str = None,
        buyer_id: str = None,
        valid_start_time: str = None,
        valid_end_time: str = None,
    ):
        self.commodity_code = commodity_code
        self.current_inventory = current_inventory
        self.inventory_id = inventory_id
        self.instance_id = instance_id
        self.buyer_id = buyer_id
        self.valid_start_time = valid_start_time
        self.valid_end_time = valid_end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.current_inventory is not None:
            result['CurrentInventory'] = self.current_inventory
        if self.inventory_id is not None:
            result['InventoryId'] = self.inventory_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.buyer_id is not None:
            result['BuyerId'] = self.buyer_id
        if self.valid_start_time is not None:
            result['ValidStartTime'] = self.valid_start_time
        if self.valid_end_time is not None:
            result['ValidEndTime'] = self.valid_end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CurrentInventory') is not None:
            self.current_inventory = m.get('CurrentInventory')
        if m.get('InventoryId') is not None:
            self.inventory_id = m.get('InventoryId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('BuyerId') is not None:
            self.buyer_id = m.get('BuyerId')
        if m.get('ValidStartTime') is not None:
            self.valid_start_time = m.get('ValidStartTime')
        if m.get('ValidEndTime') is not None:
            self.valid_end_time = m.get('ValidEndTime')
        return self


class GetInventoryResponseBodyData(TeaModel):
    def __init__(
        self,
        result_object: List[GetInventoryResponseBodyDataResultObject] = None,
    ):
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            for k in self.result_object:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResultObject'] = []
        if self.result_object is not None:
            for k in self.result_object:
                result['ResultObject'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result_object = []
        if m.get('ResultObject') is not None:
            for k in m.get('ResultObject'):
                temp_model = GetInventoryResponseBodyDataResultObject()
                self.result_object.append(temp_model.from_map(k))
        return self


class GetInventoryResponseBody(TeaModel):
    def __init__(
        self,
        data: GetInventoryResponseBodyData = None,
        success: bool = None,
    ):
        self.data = data
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetInventoryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInventoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInventoryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetInventoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMonitorListRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.corp_id = corp_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetMonitorListResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        status: str = None,
        rule_expression: str = None,
        image_match: str = None,
        monitor_type: str = None,
        create_date: str = None,
        rule_name: str = None,
        notifier_type: str = None,
        description: str = None,
        expression: str = None,
        notifier_extend_values: str = None,
        attributes: str = None,
        device_list: str = None,
        task_id: str = None,
        modified_date: str = None,
        algorithm_vendor: str = None,
    ):
        self.status = status
        self.rule_expression = rule_expression
        self.image_match = image_match
        self.monitor_type = monitor_type
        self.create_date = create_date
        self.rule_name = rule_name
        self.notifier_type = notifier_type
        self.description = description
        self.expression = expression
        self.notifier_extend_values = notifier_extend_values
        self.attributes = attributes
        self.device_list = device_list
        self.task_id = task_id
        self.modified_date = modified_date
        self.algorithm_vendor = algorithm_vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.rule_expression is not None:
            result['RuleExpression'] = self.rule_expression
        if self.image_match is not None:
            result['ImageMatch'] = self.image_match
        if self.monitor_type is not None:
            result['MonitorType'] = self.monitor_type
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.notifier_type is not None:
            result['NotifierType'] = self.notifier_type
        if self.description is not None:
            result['Description'] = self.description
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.notifier_extend_values is not None:
            result['NotifierExtendValues'] = self.notifier_extend_values
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.device_list is not None:
            result['DeviceList'] = self.device_list
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.modified_date is not None:
            result['ModifiedDate'] = self.modified_date
        if self.algorithm_vendor is not None:
            result['AlgorithmVendor'] = self.algorithm_vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RuleExpression') is not None:
            self.rule_expression = m.get('RuleExpression')
        if m.get('ImageMatch') is not None:
            self.image_match = m.get('ImageMatch')
        if m.get('MonitorType') is not None:
            self.monitor_type = m.get('MonitorType')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('NotifierType') is not None:
            self.notifier_type = m.get('NotifierType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('NotifierExtendValues') is not None:
            self.notifier_extend_values = m.get('NotifierExtendValues')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('DeviceList') is not None:
            self.device_list = m.get('DeviceList')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('ModifiedDate') is not None:
            self.modified_date = m.get('ModifiedDate')
        if m.get('AlgorithmVendor') is not None:
            self.algorithm_vendor = m.get('AlgorithmVendor')
        return self


class GetMonitorListResponseBodyData(TeaModel):
    def __init__(
        self,
        records: List[GetMonitorListResponseBodyDataRecords] = None,
        page_number: int = None,
        total_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.records = records
        self.page_number = page_number
        self.total_page = total_page
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = GetMonitorListResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetMonitorListResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetMonitorListResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetMonitorListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetMonitorListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMonitorListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetMonitorListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMonitorResultRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        task_id: str = None,
        min_record_id: str = None,
        start_time: int = None,
        end_time: int = None,
        algorithm_vendor: str = None,
    ):
        self.corp_id = corp_id
        self.task_id = task_id
        self.min_record_id = min_record_id
        self.start_time = start_time
        self.end_time = end_time
        self.algorithm_vendor = algorithm_vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.min_record_id is not None:
            result['MinRecordId'] = self.min_record_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.algorithm_vendor is not None:
            result['AlgorithmVendor'] = self.algorithm_vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('MinRecordId') is not None:
            self.min_record_id = m.get('MinRecordId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('AlgorithmVendor') is not None:
            self.algorithm_vendor = m.get('AlgorithmVendor')
        return self


class GetMonitorResultResponseBodyDataRecordsExtendInfo(TeaModel):
    def __init__(
        self,
        plate_no: str = None,
    ):
        self.plate_no = plate_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plate_no is not None:
            result['PlateNo'] = self.plate_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlateNo') is not None:
            self.plate_no = m.get('PlateNo')
        return self


class GetMonitorResultResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        pic_url: str = None,
        right_bottom_y: str = None,
        score: str = None,
        monitor_pic_url: str = None,
        right_bottom_x: str = None,
        extend_info: GetMonitorResultResponseBodyDataRecordsExtendInfo = None,
        gb_id: str = None,
        left_up_y: str = None,
        left_up_x: str = None,
        shot_time: str = None,
        task_id: str = None,
        target_pic_url: str = None,
    ):
        self.pic_url = pic_url
        self.right_bottom_y = right_bottom_y
        self.score = score
        self.monitor_pic_url = monitor_pic_url
        self.right_bottom_x = right_bottom_x
        self.extend_info = extend_info
        self.gb_id = gb_id
        self.left_up_y = left_up_y
        self.left_up_x = left_up_x
        self.shot_time = shot_time
        self.task_id = task_id
        self.target_pic_url = target_pic_url

    def validate(self):
        if self.extend_info:
            self.extend_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.right_bottom_y is not None:
            result['RightBottomY'] = self.right_bottom_y
        if self.score is not None:
            result['Score'] = self.score
        if self.monitor_pic_url is not None:
            result['MonitorPicUrl'] = self.monitor_pic_url
        if self.right_bottom_x is not None:
            result['RightBottomX'] = self.right_bottom_x
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info.to_map()
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.left_up_y is not None:
            result['LeftUpY'] = self.left_up_y
        if self.left_up_x is not None:
            result['LeftUpX'] = self.left_up_x
        if self.shot_time is not None:
            result['ShotTime'] = self.shot_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.target_pic_url is not None:
            result['TargetPicUrl'] = self.target_pic_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('RightBottomY') is not None:
            self.right_bottom_y = m.get('RightBottomY')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('MonitorPicUrl') is not None:
            self.monitor_pic_url = m.get('MonitorPicUrl')
        if m.get('RightBottomX') is not None:
            self.right_bottom_x = m.get('RightBottomX')
        if m.get('ExtendInfo') is not None:
            temp_model = GetMonitorResultResponseBodyDataRecordsExtendInfo()
            self.extend_info = temp_model.from_map(m['ExtendInfo'])
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('LeftUpY') is not None:
            self.left_up_y = m.get('LeftUpY')
        if m.get('LeftUpX') is not None:
            self.left_up_x = m.get('LeftUpX')
        if m.get('ShotTime') is not None:
            self.shot_time = m.get('ShotTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TargetPicUrl') is not None:
            self.target_pic_url = m.get('TargetPicUrl')
        return self


class GetMonitorResultResponseBodyData(TeaModel):
    def __init__(
        self,
        max_id: str = None,
        records: List[GetMonitorResultResponseBodyDataRecords] = None,
    ):
        self.max_id = max_id
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_id is not None:
            result['MaxId'] = self.max_id
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxId') is not None:
            self.max_id = m.get('MaxId')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = GetMonitorResultResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        return self


class GetMonitorResultResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetMonitorResultResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetMonitorResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetMonitorResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMonitorResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetMonitorResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPersonDetailRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        person_id: str = None,
        algorithm_type: str = None,
    ):
        self.corp_id = corp_id
        self.person_id = person_id
        self.algorithm_type = algorithm_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.person_id is not None:
            result['PersonID'] = self.person_id
        if self.algorithm_type is not None:
            result['AlgorithmType'] = self.algorithm_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('PersonID') is not None:
            self.person_id = m.get('PersonID')
        if m.get('AlgorithmType') is not None:
            self.algorithm_type = m.get('AlgorithmType')
        return self


class GetPersonDetailResponseBodyDataTagList(TeaModel):
    def __init__(
        self,
        tag_value_id: str = None,
        tag_name: str = None,
        tag_code: str = None,
        tag_value: str = None,
    ):
        self.tag_value_id = tag_value_id
        self.tag_name = tag_name
        self.tag_code = tag_code
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_value_id is not None:
            result['TagValueId'] = self.tag_value_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.tag_code is not None:
            result['TagCode'] = self.tag_code
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagValueId') is not None:
            self.tag_value_id = m.get('TagValueId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TagCode') is not None:
            self.tag_code = m.get('TagCode')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class GetPersonDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        pic_url: str = None,
        tag_list: List[GetPersonDetailResponseBodyDataTagList] = None,
        person_id: str = None,
    ):
        self.pic_url = pic_url
        self.tag_list = tag_list
        self.person_id = person_id

    def validate(self):
        if self.tag_list:
            for k in self.tag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        result['TagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['TagList'].append(k.to_map() if k else None)
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        self.tag_list = []
        if m.get('TagList') is not None:
            for k in m.get('TagList'):
                temp_model = GetPersonDetailResponseBodyDataTagList()
                self.tag_list.append(temp_model.from_map(k))
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        return self


class GetPersonDetailResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetPersonDetailResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetPersonDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetPersonDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPersonDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetPersonDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPersonListRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        face_url: str = None,
        corp_id_list: Dict[str, Any] = None,
        face_matching_rate_threshold: str = None,
        corp_id: str = None,
        person_id_list: Dict[str, Any] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.face_url = face_url
        self.corp_id_list = corp_id_list
        self.face_matching_rate_threshold = face_matching_rate_threshold
        self.corp_id = corp_id
        self.person_id_list = person_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.face_url is not None:
            result['FaceUrl'] = self.face_url
        if self.corp_id_list is not None:
            result['CorpIdList'] = self.corp_id_list
        if self.face_matching_rate_threshold is not None:
            result['FaceMatchingRateThreshold'] = self.face_matching_rate_threshold
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.person_id_list is not None:
            result['PersonIdList'] = self.person_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')
        if m.get('CorpIdList') is not None:
            self.corp_id_list = m.get('CorpIdList')
        if m.get('FaceMatchingRateThreshold') is not None:
            self.face_matching_rate_threshold = m.get('FaceMatchingRateThreshold')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('PersonIdList') is not None:
            self.person_id_list = m.get('PersonIdList')
        return self


class GetPersonListShrinkRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        face_url: str = None,
        corp_id_list_shrink: str = None,
        face_matching_rate_threshold: str = None,
        corp_id: str = None,
        person_id_list_shrink: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.face_url = face_url
        self.corp_id_list_shrink = corp_id_list_shrink
        self.face_matching_rate_threshold = face_matching_rate_threshold
        self.corp_id = corp_id
        self.person_id_list_shrink = person_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.face_url is not None:
            result['FaceUrl'] = self.face_url
        if self.corp_id_list_shrink is not None:
            result['CorpIdList'] = self.corp_id_list_shrink
        if self.face_matching_rate_threshold is not None:
            result['FaceMatchingRateThreshold'] = self.face_matching_rate_threshold
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.person_id_list_shrink is not None:
            result['PersonIdList'] = self.person_id_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')
        if m.get('CorpIdList') is not None:
            self.corp_id_list_shrink = m.get('CorpIdList')
        if m.get('FaceMatchingRateThreshold') is not None:
            self.face_matching_rate_threshold = m.get('FaceMatchingRateThreshold')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('PersonIdList') is not None:
            self.person_id_list_shrink = m.get('PersonIdList')
        return self


class GetPersonListResponseBodyDataRecordsPropertyTagList(TeaModel):
    def __init__(
        self,
        value: str = None,
        tag_name: str = None,
        tag_code_name: str = None,
        code: str = None,
    ):
        self.value = value
        self.tag_name = tag_name
        self.tag_code_name = tag_code_name
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.tag_code_name is not None:
            result['TagCodeName'] = self.tag_code_name
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TagCodeName') is not None:
            self.tag_code_name = m.get('TagCodeName')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetPersonListResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        property_tag_list: List[GetPersonListResponseBodyDataRecordsPropertyTagList] = None,
        face_url: str = None,
        search_matching_rate: str = None,
        person_id: str = None,
        last_shot_time: int = None,
        first_shot_time: int = None,
    ):
        self.property_tag_list = property_tag_list
        self.face_url = face_url
        self.search_matching_rate = search_matching_rate
        self.person_id = person_id
        self.last_shot_time = last_shot_time
        self.first_shot_time = first_shot_time

    def validate(self):
        if self.property_tag_list:
            for k in self.property_tag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PropertyTagList'] = []
        if self.property_tag_list is not None:
            for k in self.property_tag_list:
                result['PropertyTagList'].append(k.to_map() if k else None)
        if self.face_url is not None:
            result['FaceUrl'] = self.face_url
        if self.search_matching_rate is not None:
            result['SearchMatchingRate'] = self.search_matching_rate
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.last_shot_time is not None:
            result['LastShotTime'] = self.last_shot_time
        if self.first_shot_time is not None:
            result['FirstShotTime'] = self.first_shot_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.property_tag_list = []
        if m.get('PropertyTagList') is not None:
            for k in m.get('PropertyTagList'):
                temp_model = GetPersonListResponseBodyDataRecordsPropertyTagList()
                self.property_tag_list.append(temp_model.from_map(k))
        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')
        if m.get('SearchMatchingRate') is not None:
            self.search_matching_rate = m.get('SearchMatchingRate')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('LastShotTime') is not None:
            self.last_shot_time = m.get('LastShotTime')
        if m.get('FirstShotTime') is not None:
            self.first_shot_time = m.get('FirstShotTime')
        return self


class GetPersonListResponseBodyData(TeaModel):
    def __init__(
        self,
        records: List[GetPersonListResponseBodyDataRecords] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.records = records
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = GetPersonListResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetPersonListResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetPersonListResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetPersonListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetPersonListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPersonListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetPersonListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPictureUrlRequest(TeaModel):
    def __init__(
        self,
        origin_url: str = None,
        expire_time: str = None,
    ):
        self.origin_url = origin_url
        self.expire_time = expire_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.origin_url is not None:
            result['OriginUrl'] = self.origin_url
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginUrl') is not None:
            self.origin_url = m.get('OriginUrl')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        return self


class GetPictureUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        url: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.url = url
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.url is not None:
            result['Url'] = self.url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPictureUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPictureUrlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetPictureUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProfileDetailRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        isv_sub_id: str = None,
        profile_id: int = None,
    ):
        self.corp_id = corp_id
        self.isv_sub_id = isv_sub_id
        self.profile_id = profile_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.profile_id is not None:
            result['ProfileId'] = self.profile_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('ProfileId') is not None:
            self.profile_id = m.get('ProfileId')
        return self


class GetProfileDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        catalog_id: int = None,
        profile_id: int = None,
        isv_sub_id: str = None,
        gender: str = None,
        biz_id: str = None,
        id_number: str = None,
        scene_type: str = None,
        phone_no: str = None,
        face_url: str = None,
        live_address: str = None,
        name: str = None,
        person_id: str = None,
        plate_no: str = None,
    ):
        self.catalog_id = catalog_id
        self.profile_id = profile_id
        self.isv_sub_id = isv_sub_id
        self.gender = gender
        self.biz_id = biz_id
        self.id_number = id_number
        self.scene_type = scene_type
        self.phone_no = phone_no
        self.face_url = face_url
        self.live_address = live_address
        self.name = name
        self.person_id = person_id
        self.plate_no = plate_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.profile_id is not None:
            result['ProfileId'] = self.profile_id
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.id_number is not None:
            result['IdNumber'] = self.id_number
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        if self.face_url is not None:
            result['FaceUrl'] = self.face_url
        if self.live_address is not None:
            result['LiveAddress'] = self.live_address
        if self.name is not None:
            result['Name'] = self.name
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.plate_no is not None:
            result['PlateNo'] = self.plate_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('ProfileId') is not None:
            self.profile_id = m.get('ProfileId')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('IdNumber') is not None:
            self.id_number = m.get('IdNumber')
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')
        if m.get('LiveAddress') is not None:
            self.live_address = m.get('LiveAddress')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('PlateNo') is not None:
            self.plate_no = m.get('PlateNo')
        return self


class GetProfileDetailResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetProfileDetailResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetProfileDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetProfileDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetProfileDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetProfileDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProfileListRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        isv_sub_id: str = None,
        name: str = None,
        catalog_id: int = None,
        id_number: str = None,
        face_url: str = None,
        live_address: str = None,
        gender: int = None,
        plate_no: str = None,
        phone_no: str = None,
        scene_type: str = None,
        biz_id: str = None,
        page_number: int = None,
        page_size: int = None,
        person_id_list: Dict[str, Any] = None,
        profile_id_list: Dict[str, Any] = None,
        matching_rate_threshold: str = None,
        face_image_id: str = None,
    ):
        self.corp_id = corp_id
        self.isv_sub_id = isv_sub_id
        self.name = name
        self.catalog_id = catalog_id
        self.id_number = id_number
        self.face_url = face_url
        self.live_address = live_address
        self.gender = gender
        self.plate_no = plate_no
        self.phone_no = phone_no
        self.scene_type = scene_type
        self.biz_id = biz_id
        self.page_number = page_number
        self.page_size = page_size
        self.person_id_list = person_id_list
        self.profile_id_list = profile_id_list
        self.matching_rate_threshold = matching_rate_threshold
        self.face_image_id = face_image_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.name is not None:
            result['Name'] = self.name
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.id_number is not None:
            result['IdNumber'] = self.id_number
        if self.face_url is not None:
            result['FaceUrl'] = self.face_url
        if self.live_address is not None:
            result['LiveAddress'] = self.live_address
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.plate_no is not None:
            result['PlateNo'] = self.plate_no
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.person_id_list is not None:
            result['PersonIdList'] = self.person_id_list
        if self.profile_id_list is not None:
            result['ProfileIdList'] = self.profile_id_list
        if self.matching_rate_threshold is not None:
            result['MatchingRateThreshold'] = self.matching_rate_threshold
        if self.face_image_id is not None:
            result['FaceImageId'] = self.face_image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('IdNumber') is not None:
            self.id_number = m.get('IdNumber')
        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')
        if m.get('LiveAddress') is not None:
            self.live_address = m.get('LiveAddress')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('PlateNo') is not None:
            self.plate_no = m.get('PlateNo')
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PersonIdList') is not None:
            self.person_id_list = m.get('PersonIdList')
        if m.get('ProfileIdList') is not None:
            self.profile_id_list = m.get('ProfileIdList')
        if m.get('MatchingRateThreshold') is not None:
            self.matching_rate_threshold = m.get('MatchingRateThreshold')
        if m.get('FaceImageId') is not None:
            self.face_image_id = m.get('FaceImageId')
        return self


class GetProfileListShrinkRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        isv_sub_id: str = None,
        name: str = None,
        catalog_id: int = None,
        id_number: str = None,
        face_url: str = None,
        live_address: str = None,
        gender: int = None,
        plate_no: str = None,
        phone_no: str = None,
        scene_type: str = None,
        biz_id: str = None,
        page_number: int = None,
        page_size: int = None,
        person_id_list_shrink: str = None,
        profile_id_list_shrink: str = None,
        matching_rate_threshold: str = None,
        face_image_id: str = None,
    ):
        self.corp_id = corp_id
        self.isv_sub_id = isv_sub_id
        self.name = name
        self.catalog_id = catalog_id
        self.id_number = id_number
        self.face_url = face_url
        self.live_address = live_address
        self.gender = gender
        self.plate_no = plate_no
        self.phone_no = phone_no
        self.scene_type = scene_type
        self.biz_id = biz_id
        self.page_number = page_number
        self.page_size = page_size
        self.person_id_list_shrink = person_id_list_shrink
        self.profile_id_list_shrink = profile_id_list_shrink
        self.matching_rate_threshold = matching_rate_threshold
        self.face_image_id = face_image_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.name is not None:
            result['Name'] = self.name
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.id_number is not None:
            result['IdNumber'] = self.id_number
        if self.face_url is not None:
            result['FaceUrl'] = self.face_url
        if self.live_address is not None:
            result['LiveAddress'] = self.live_address
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.plate_no is not None:
            result['PlateNo'] = self.plate_no
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.person_id_list_shrink is not None:
            result['PersonIdList'] = self.person_id_list_shrink
        if self.profile_id_list_shrink is not None:
            result['ProfileIdList'] = self.profile_id_list_shrink
        if self.matching_rate_threshold is not None:
            result['MatchingRateThreshold'] = self.matching_rate_threshold
        if self.face_image_id is not None:
            result['FaceImageId'] = self.face_image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('IdNumber') is not None:
            self.id_number = m.get('IdNumber')
        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')
        if m.get('LiveAddress') is not None:
            self.live_address = m.get('LiveAddress')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('PlateNo') is not None:
            self.plate_no = m.get('PlateNo')
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PersonIdList') is not None:
            self.person_id_list_shrink = m.get('PersonIdList')
        if m.get('ProfileIdList') is not None:
            self.profile_id_list_shrink = m.get('ProfileIdList')
        if m.get('MatchingRateThreshold') is not None:
            self.matching_rate_threshold = m.get('MatchingRateThreshold')
        if m.get('FaceImageId') is not None:
            self.face_image_id = m.get('FaceImageId')
        return self


class GetProfileListResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        catalog_id: int = None,
        profile_id: int = None,
        id_number: str = None,
        scene_type: str = None,
        isv_sub_id: str = None,
        gender: str = None,
        face_url: str = None,
        biz_id: str = None,
        search_matching_rate: str = None,
        name: str = None,
        person_id: str = None,
    ):
        self.catalog_id = catalog_id
        self.profile_id = profile_id
        self.id_number = id_number
        self.scene_type = scene_type
        self.isv_sub_id = isv_sub_id
        self.gender = gender
        self.face_url = face_url
        self.biz_id = biz_id
        self.search_matching_rate = search_matching_rate
        self.name = name
        self.person_id = person_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.profile_id is not None:
            result['ProfileId'] = self.profile_id
        if self.id_number is not None:
            result['IdNumber'] = self.id_number
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.face_url is not None:
            result['FaceUrl'] = self.face_url
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.search_matching_rate is not None:
            result['SearchMatchingRate'] = self.search_matching_rate
        if self.name is not None:
            result['Name'] = self.name
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('ProfileId') is not None:
            self.profile_id = m.get('ProfileId')
        if m.get('IdNumber') is not None:
            self.id_number = m.get('IdNumber')
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('SearchMatchingRate') is not None:
            self.search_matching_rate = m.get('SearchMatchingRate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        return self


class GetProfileListResponseBodyData(TeaModel):
    def __init__(
        self,
        success: bool = None,
        records: List[GetProfileListResponseBodyDataRecords] = None,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.success = success
        self.records = records
        self.page_number = page_number
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = GetProfileListResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetProfileListResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetProfileListResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetProfileListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetProfileListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetProfileListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetProfileListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrainAlgorithRequest(TeaModel):
    def __init__(
        self,
        algorithm_id: str = None,
        version: str = None,
    ):
        self.algorithm_id = algorithm_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetTrainAlgorithResponseBodyDataInstanceList(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        instace_id: str = None,
        project_id: str = None,
    ):
        self.instance_name = instance_name
        self.instace_id = instace_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instace_id is not None:
            result['InstaceId'] = self.instace_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstaceId') is not None:
            self.instace_id = m.get('InstaceId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetTrainAlgorithResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
        algorithm_name: str = None,
        user_id: str = None,
        algorithm_type: str = None,
        train_sample_count: int = None,
        test_sample_count: int = None,
        deleted: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        train_status: str = None,
        train_progress: int = None,
        train_queue_size: int = None,
        train_estimate_time: int = None,
        deploy_status: str = None,
        ready_train: str = None,
        deploy_version: str = None,
        precision: float = None,
        recall: float = None,
        no_ready_reason: str = None,
        instance_list: List[GetTrainAlgorithResponseBodyDataInstanceList] = None,
    ):
        self.id = id
        self.algorithm_name = algorithm_name
        self.user_id = user_id
        self.algorithm_type = algorithm_type
        self.train_sample_count = train_sample_count
        self.test_sample_count = test_sample_count
        self.deleted = deleted
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.train_status = train_status
        self.train_progress = train_progress
        self.train_queue_size = train_queue_size
        self.train_estimate_time = train_estimate_time
        self.deploy_status = deploy_status
        self.ready_train = ready_train
        self.deploy_version = deploy_version
        self.precision = precision
        self.recall = recall
        self.no_ready_reason = no_ready_reason
        self.instance_list = instance_list

    def validate(self):
        if self.instance_list:
            for k in self.instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.algorithm_type is not None:
            result['AlgorithmType'] = self.algorithm_type
        if self.train_sample_count is not None:
            result['TrainSampleCount'] = self.train_sample_count
        if self.test_sample_count is not None:
            result['TestSampleCount'] = self.test_sample_count
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.train_status is not None:
            result['TrainStatus'] = self.train_status
        if self.train_progress is not None:
            result['TrainProgress'] = self.train_progress
        if self.train_queue_size is not None:
            result['TrainQueueSize'] = self.train_queue_size
        if self.train_estimate_time is not None:
            result['TrainEstimateTime'] = self.train_estimate_time
        if self.deploy_status is not None:
            result['DeployStatus'] = self.deploy_status
        if self.ready_train is not None:
            result['ReadyTrain'] = self.ready_train
        if self.deploy_version is not None:
            result['DeployVersion'] = self.deploy_version
        if self.precision is not None:
            result['Precision'] = self.precision
        if self.recall is not None:
            result['Recall'] = self.recall
        if self.no_ready_reason is not None:
            result['NoReadyReason'] = self.no_ready_reason
        result['InstanceList'] = []
        if self.instance_list is not None:
            for k in self.instance_list:
                result['InstanceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('AlgorithmType') is not None:
            self.algorithm_type = m.get('AlgorithmType')
        if m.get('TrainSampleCount') is not None:
            self.train_sample_count = m.get('TrainSampleCount')
        if m.get('TestSampleCount') is not None:
            self.test_sample_count = m.get('TestSampleCount')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('TrainStatus') is not None:
            self.train_status = m.get('TrainStatus')
        if m.get('TrainProgress') is not None:
            self.train_progress = m.get('TrainProgress')
        if m.get('TrainQueueSize') is not None:
            self.train_queue_size = m.get('TrainQueueSize')
        if m.get('TrainEstimateTime') is not None:
            self.train_estimate_time = m.get('TrainEstimateTime')
        if m.get('DeployStatus') is not None:
            self.deploy_status = m.get('DeployStatus')
        if m.get('ReadyTrain') is not None:
            self.ready_train = m.get('ReadyTrain')
        if m.get('DeployVersion') is not None:
            self.deploy_version = m.get('DeployVersion')
        if m.get('Precision') is not None:
            self.precision = m.get('Precision')
        if m.get('Recall') is not None:
            self.recall = m.get('Recall')
        if m.get('NoReadyReason') is not None:
            self.no_ready_reason = m.get('NoReadyReason')
        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k in m.get('InstanceList'):
                temp_model = GetTrainAlgorithResponseBodyDataInstanceList()
                self.instance_list.append(temp_model.from_map(k))
        return self


class GetTrainAlgorithResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        data: GetTrainAlgorithResponseBodyData = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = GetTrainAlgorithResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetTrainAlgorithResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTrainAlgorithResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetTrainAlgorithResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrainAlgorithmRequest(TeaModel):
    def __init__(
        self,
        algorithm_id: str = None,
        algorithm_version: str = None,
    ):
        self.algorithm_id = algorithm_id
        self.algorithm_version = algorithm_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.algorithm_version is not None:
            result['AlgorithmVersion'] = self.algorithm_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('AlgorithmVersion') is not None:
            self.algorithm_version = m.get('AlgorithmVersion')
        return self


class GetTrainAlgorithmResponseBodyDataInstanceList(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        instace_id: str = None,
        project_id: str = None,
    ):
        self.instance_name = instance_name
        self.instace_id = instace_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instace_id is not None:
            result['InstaceId'] = self.instace_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstaceId') is not None:
            self.instace_id = m.get('InstaceId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetTrainAlgorithmResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
        algorithm_name: str = None,
        user_id: str = None,
        algorithm_type: str = None,
        train_sample_count: int = None,
        test_sample_count: int = None,
        deleted: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        train_status: str = None,
        train_progress: int = None,
        train_queue_size: int = None,
        train_estimate_time: int = None,
        deploy_status: str = None,
        ready_train: str = None,
        deploy_version: str = None,
        precision: float = None,
        recall: float = None,
        train_time: str = None,
        deploy_time: str = None,
        current_version: str = None,
        no_ready_reason: str = None,
        can_unpublish: str = None,
        instance_list: List[GetTrainAlgorithmResponseBodyDataInstanceList] = None,
    ):
        self.id = id
        self.algorithm_name = algorithm_name
        self.user_id = user_id
        self.algorithm_type = algorithm_type
        self.train_sample_count = train_sample_count
        self.test_sample_count = test_sample_count
        self.deleted = deleted
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.train_status = train_status
        self.train_progress = train_progress
        self.train_queue_size = train_queue_size
        self.train_estimate_time = train_estimate_time
        self.deploy_status = deploy_status
        self.ready_train = ready_train
        self.deploy_version = deploy_version
        self.precision = precision
        self.recall = recall
        self.train_time = train_time
        self.deploy_time = deploy_time
        self.current_version = current_version
        self.no_ready_reason = no_ready_reason
        self.can_unpublish = can_unpublish
        self.instance_list = instance_list

    def validate(self):
        if self.instance_list:
            for k in self.instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.algorithm_type is not None:
            result['AlgorithmType'] = self.algorithm_type
        if self.train_sample_count is not None:
            result['TrainSampleCount'] = self.train_sample_count
        if self.test_sample_count is not None:
            result['TestSampleCount'] = self.test_sample_count
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.train_status is not None:
            result['TrainStatus'] = self.train_status
        if self.train_progress is not None:
            result['TrainProgress'] = self.train_progress
        if self.train_queue_size is not None:
            result['TrainQueueSize'] = self.train_queue_size
        if self.train_estimate_time is not None:
            result['TrainEstimateTime'] = self.train_estimate_time
        if self.deploy_status is not None:
            result['DeployStatus'] = self.deploy_status
        if self.ready_train is not None:
            result['ReadyTrain'] = self.ready_train
        if self.deploy_version is not None:
            result['DeployVersion'] = self.deploy_version
        if self.precision is not None:
            result['Precision'] = self.precision
        if self.recall is not None:
            result['Recall'] = self.recall
        if self.train_time is not None:
            result['TrainTime'] = self.train_time
        if self.deploy_time is not None:
            result['DeployTime'] = self.deploy_time
        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version
        if self.no_ready_reason is not None:
            result['NoReadyReason'] = self.no_ready_reason
        if self.can_unpublish is not None:
            result['CanUnpublish'] = self.can_unpublish
        result['InstanceList'] = []
        if self.instance_list is not None:
            for k in self.instance_list:
                result['InstanceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('AlgorithmType') is not None:
            self.algorithm_type = m.get('AlgorithmType')
        if m.get('TrainSampleCount') is not None:
            self.train_sample_count = m.get('TrainSampleCount')
        if m.get('TestSampleCount') is not None:
            self.test_sample_count = m.get('TestSampleCount')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('TrainStatus') is not None:
            self.train_status = m.get('TrainStatus')
        if m.get('TrainProgress') is not None:
            self.train_progress = m.get('TrainProgress')
        if m.get('TrainQueueSize') is not None:
            self.train_queue_size = m.get('TrainQueueSize')
        if m.get('TrainEstimateTime') is not None:
            self.train_estimate_time = m.get('TrainEstimateTime')
        if m.get('DeployStatus') is not None:
            self.deploy_status = m.get('DeployStatus')
        if m.get('ReadyTrain') is not None:
            self.ready_train = m.get('ReadyTrain')
        if m.get('DeployVersion') is not None:
            self.deploy_version = m.get('DeployVersion')
        if m.get('Precision') is not None:
            self.precision = m.get('Precision')
        if m.get('Recall') is not None:
            self.recall = m.get('Recall')
        if m.get('TrainTime') is not None:
            self.train_time = m.get('TrainTime')
        if m.get('DeployTime') is not None:
            self.deploy_time = m.get('DeployTime')
        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')
        if m.get('NoReadyReason') is not None:
            self.no_ready_reason = m.get('NoReadyReason')
        if m.get('CanUnpublish') is not None:
            self.can_unpublish = m.get('CanUnpublish')
        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k in m.get('InstanceList'):
                temp_model = GetTrainAlgorithmResponseBodyDataInstanceList()
                self.instance_list.append(temp_model.from_map(k))
        return self


class GetTrainAlgorithmResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        data: GetTrainAlgorithmResponseBodyData = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = GetTrainAlgorithmResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetTrainAlgorithmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTrainAlgorithmResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetTrainAlgorithmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrainLabelRequest(TeaModel):
    def __init__(
        self,
        label_id: str = None,
    ):
        self.label_id = label_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        return self


class GetTrainLabelResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
        label_name: str = None,
        algorithm_id: str = None,
        train_marker_cnt: int = None,
        test_marker_cnt: int = None,
        deleted: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
    ):
        self.id = id
        self.label_name = label_name
        self.algorithm_id = algorithm_id
        self.train_marker_cnt = train_marker_cnt
        self.test_marker_cnt = test_marker_cnt
        self.deleted = deleted
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['ID'] = self.id
        if self.label_name is not None:
            result['LabelName'] = self.label_name
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.train_marker_cnt is not None:
            result['TrainMarkerCnt'] = self.train_marker_cnt
        if self.test_marker_cnt is not None:
            result['TestMarkerCnt'] = self.test_marker_cnt
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ID') is not None:
            self.id = m.get('ID')
        if m.get('LabelName') is not None:
            self.label_name = m.get('LabelName')
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('TrainMarkerCnt') is not None:
            self.train_marker_cnt = m.get('TrainMarkerCnt')
        if m.get('TestMarkerCnt') is not None:
            self.test_marker_cnt = m.get('TestMarkerCnt')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        return self


class GetTrainLabelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        data: GetTrainLabelResponseBodyData = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = GetTrainLabelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetTrainLabelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTrainLabelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetTrainLabelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserDetailRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        isv_sub_id: str = None,
        user_id: int = None,
        need_face_detail: bool = None,
    ):
        self.corp_id = corp_id
        self.isv_sub_id = isv_sub_id
        self.user_id = user_id
        self.need_face_detail = need_face_detail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.need_face_detail is not None:
            result['NeedFaceDetail'] = self.need_face_detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('NeedFaceDetail') is not None:
            self.need_face_detail = m.get('NeedFaceDetail')
        return self


class GetUserDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        gender: str = None,
        face_image_url: str = None,
        isv_sub_id: str = None,
        user_group_id: int = None,
        user_id: int = None,
        biz_id: str = None,
        attachment: str = None,
        age: str = None,
        id_number: str = None,
        phone_no: str = None,
        address: str = None,
        user_name: str = None,
        plate_no: str = None,
    ):
        self.gender = gender
        self.face_image_url = face_image_url
        self.isv_sub_id = isv_sub_id
        self.user_group_id = user_group_id
        self.user_id = user_id
        self.biz_id = biz_id
        self.attachment = attachment
        self.age = age
        self.id_number = id_number
        self.phone_no = phone_no
        self.address = address
        self.user_name = user_name
        self.plate_no = plate_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.attachment is not None:
            result['Attachment'] = self.attachment
        if self.age is not None:
            result['Age'] = self.age
        if self.id_number is not None:
            result['IdNumber'] = self.id_number
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        if self.address is not None:
            result['Address'] = self.address
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.plate_no is not None:
            result['PlateNo'] = self.plate_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Attachment') is not None:
            self.attachment = m.get('Attachment')
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('IdNumber') is not None:
            self.id_number = m.get('IdNumber')
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('PlateNo') is not None:
            self.plate_no = m.get('PlateNo')
        return self


class GetUserDetailResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetUserDetailResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetUserDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetUserDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetUserDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoComposeResultRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        task_request_id: str = None,
    ):
        self.corp_id = corp_id
        self.task_request_id = task_request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.task_request_id is not None:
            result['TaskRequestId'] = self.task_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TaskRequestId') is not None:
            self.task_request_id = m.get('TaskRequestId')
        return self


class GetVideoComposeResultResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
        video_url: str = None,
    ):
        self.status = status
        self.message = message
        self.request_id = request_id
        self.code = code
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class GetVideoComposeResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetVideoComposeResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetVideoComposeResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoSummaryTaskResultRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        task_id: str = None,
    ):
        self.corp_id = corp_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetVideoSummaryTaskResultResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetVideoSummaryTaskResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetVideoSummaryTaskResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetVideoSummaryTaskResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InvokeMotorModelRequest(TeaModel):
    def __init__(
        self,
        pic_id: str = None,
        corp_id: str = None,
        pic_path: str = None,
        pic_url: str = None,
    ):
        self.pic_id = pic_id
        self.corp_id = corp_id
        self.pic_path = pic_path
        self.pic_url = pic_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_id is not None:
            result['PicId'] = self.pic_id
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.pic_path is not None:
            result['PicPath'] = self.pic_path
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicId') is not None:
            self.pic_id = m.get('PicId')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('PicPath') is not None:
            self.pic_path = m.get('PicPath')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        return self


class InvokeMotorModelResponseBodyData(TeaModel):
    def __init__(
        self,
        struct_list: str = None,
    ):
        self.struct_list = struct_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.struct_list is not None:
            result['StructList'] = self.struct_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StructList') is not None:
            self.struct_list = m.get('StructList')
        return self


class InvokeMotorModelResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: InvokeMotorModelResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = InvokeMotorModelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class InvokeMotorModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InvokeMotorModelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InvokeMotorModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccessNumberRequest(TeaModel):
    def __init__(
        self,
        corp_id_list: str = None,
    ):
        self.corp_id_list = corp_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id_list is not None:
            result['CorpIdList'] = self.corp_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpIdList') is not None:
            self.corp_id_list = m.get('CorpIdList')
        return self


class ListAccessNumberResponseBodyData(TeaModel):
    def __init__(
        self,
        item: str = None,
        count: str = None,
        percent: str = None,
    ):
        self.item = item
        self.count = count
        self.percent = percent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item is not None:
            result['Item'] = self.item
        if self.count is not None:
            result['Count'] = self.count
        if self.percent is not None:
            result['Percent'] = self.percent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Item') is not None:
            self.item = m.get('Item')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        return self


class ListAccessNumberResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        data: List[ListAccessNumberResponseBodyData] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAccessNumberResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class ListAccessNumberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAccessNumberResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAccessNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlgorithmNamesByDeviceIdsRequest(TeaModel):
    def __init__(
        self,
        gb_ids: str = None,
    ):
        self.gb_ids = gb_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gb_ids is not None:
            result['GbIds'] = self.gb_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GbIds') is not None:
            self.gb_ids = m.get('GbIds')
        return self


class ListAlgorithmNamesByDeviceIdsResponseBodyData(TeaModel):
    def __init__(
        self,
        gb_id: str = None,
        algorithm_names: List[str] = None,
    ):
        self.gb_id = gb_id
        self.algorithm_names = algorithm_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.algorithm_names is not None:
            result['AlgorithmNames'] = self.algorithm_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('AlgorithmNames') is not None:
            self.algorithm_names = m.get('AlgorithmNames')
        return self


class ListAlgorithmNamesByDeviceIdsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        data: List[ListAlgorithmNamesByDeviceIdsResponseBodyData] = None,
        code: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.success = success
        self.data = data
        self.code = code
        self.message = message

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAlgorithmNamesByDeviceIdsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ListAlgorithmNamesByDeviceIdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAlgorithmNamesByDeviceIdsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAlgorithmNamesByDeviceIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBodyAlgorithmResultsRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        algorithm_type: str = None,
        data_source_id: str = None,
        start_time: str = None,
        end_time: str = None,
        page_number: str = None,
        page_size: str = None,
        cap_style: str = None,
    ):
        self.corp_id = corp_id
        self.algorithm_type = algorithm_type
        self.data_source_id = data_source_id
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.cap_style = cap_style

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.algorithm_type is not None:
            result['AlgorithmType'] = self.algorithm_type
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.cap_style is not None:
            result['CapStyle'] = self.cap_style
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('AlgorithmType') is not None:
            self.algorithm_type = m.get('AlgorithmType')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CapStyle') is not None:
            self.cap_style = m.get('CapStyle')
        return self


class ListBodyAlgorithmResultsResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        right_bottom_y: float = None,
        data_source_id: str = None,
        pic_url_path: str = None,
        trousers_color: str = None,
        right_bottom_x: float = None,
        coat_color: str = None,
        source_id: str = None,
        max_age: str = None,
        coat_length: str = None,
        target_pic_url_path: str = None,
        hair_style: str = None,
        coat_style: str = None,
        left_top_y: float = None,
        min_age: str = None,
        corp_id: str = None,
        trousers_length: str = None,
        trousers_style: str = None,
        shot_time: str = None,
        left_top_x: float = None,
        gender_code: str = None,
        person_id: str = None,
        cap_style: str = None,
    ):
        self.right_bottom_y = right_bottom_y
        self.data_source_id = data_source_id
        self.pic_url_path = pic_url_path
        self.trousers_color = trousers_color
        self.right_bottom_x = right_bottom_x
        self.coat_color = coat_color
        self.source_id = source_id
        self.max_age = max_age
        self.coat_length = coat_length
        self.target_pic_url_path = target_pic_url_path
        self.hair_style = hair_style
        self.coat_style = coat_style
        self.left_top_y = left_top_y
        self.min_age = min_age
        self.corp_id = corp_id
        self.trousers_length = trousers_length
        self.trousers_style = trousers_style
        self.shot_time = shot_time
        self.left_top_x = left_top_x
        self.gender_code = gender_code
        self.person_id = person_id
        self.cap_style = cap_style

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.right_bottom_y is not None:
            result['RightBottomY'] = self.right_bottom_y
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.pic_url_path is not None:
            result['PicUrlPath'] = self.pic_url_path
        if self.trousers_color is not None:
            result['TrousersColor'] = self.trousers_color
        if self.right_bottom_x is not None:
            result['RightBottomX'] = self.right_bottom_x
        if self.coat_color is not None:
            result['CoatColor'] = self.coat_color
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.max_age is not None:
            result['MaxAge'] = self.max_age
        if self.coat_length is not None:
            result['CoatLength'] = self.coat_length
        if self.target_pic_url_path is not None:
            result['TargetPicUrlPath'] = self.target_pic_url_path
        if self.hair_style is not None:
            result['HairStyle'] = self.hair_style
        if self.coat_style is not None:
            result['CoatStyle'] = self.coat_style
        if self.left_top_y is not None:
            result['LeftTopY'] = self.left_top_y
        if self.min_age is not None:
            result['MinAge'] = self.min_age
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.trousers_length is not None:
            result['TrousersLength'] = self.trousers_length
        if self.trousers_style is not None:
            result['TrousersStyle'] = self.trousers_style
        if self.shot_time is not None:
            result['ShotTime'] = self.shot_time
        if self.left_top_x is not None:
            result['LeftTopX'] = self.left_top_x
        if self.gender_code is not None:
            result['GenderCode'] = self.gender_code
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.cap_style is not None:
            result['CapStyle'] = self.cap_style
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RightBottomY') is not None:
            self.right_bottom_y = m.get('RightBottomY')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('PicUrlPath') is not None:
            self.pic_url_path = m.get('PicUrlPath')
        if m.get('TrousersColor') is not None:
            self.trousers_color = m.get('TrousersColor')
        if m.get('RightBottomX') is not None:
            self.right_bottom_x = m.get('RightBottomX')
        if m.get('CoatColor') is not None:
            self.coat_color = m.get('CoatColor')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('MaxAge') is not None:
            self.max_age = m.get('MaxAge')
        if m.get('CoatLength') is not None:
            self.coat_length = m.get('CoatLength')
        if m.get('TargetPicUrlPath') is not None:
            self.target_pic_url_path = m.get('TargetPicUrlPath')
        if m.get('HairStyle') is not None:
            self.hair_style = m.get('HairStyle')
        if m.get('CoatStyle') is not None:
            self.coat_style = m.get('CoatStyle')
        if m.get('LeftTopY') is not None:
            self.left_top_y = m.get('LeftTopY')
        if m.get('MinAge') is not None:
            self.min_age = m.get('MinAge')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TrousersLength') is not None:
            self.trousers_length = m.get('TrousersLength')
        if m.get('TrousersStyle') is not None:
            self.trousers_style = m.get('TrousersStyle')
        if m.get('ShotTime') is not None:
            self.shot_time = m.get('ShotTime')
        if m.get('LeftTopX') is not None:
            self.left_top_x = m.get('LeftTopX')
        if m.get('GenderCode') is not None:
            self.gender_code = m.get('GenderCode')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('CapStyle') is not None:
            self.cap_style = m.get('CapStyle')
        return self


class ListBodyAlgorithmResultsResponseBodyData(TeaModel):
    def __init__(
        self,
        records: List[ListBodyAlgorithmResultsResponseBodyDataRecords] = None,
        total_page: int = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.records = records
        self.total_page = total_page
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListBodyAlgorithmResultsResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListBodyAlgorithmResultsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListBodyAlgorithmResultsResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListBodyAlgorithmResultsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListBodyAlgorithmResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListBodyAlgorithmResultsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListBodyAlgorithmResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCorpGroupMetricsRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        tag_code: str = None,
        end_time: str = None,
        group_id: str = None,
        page_number: str = None,
        page_size: str = None,
        device_id: str = None,
        corp_id: str = None,
        user_group: str = None,
        device_group: str = None,
    ):
        self.start_time = start_time
        self.tag_code = tag_code
        self.end_time = end_time
        self.group_id = group_id
        self.page_number = page_number
        self.page_size = page_size
        self.device_id = device_id
        self.corp_id = corp_id
        self.user_group = user_group
        self.device_group = device_group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tag_code is not None:
            result['TagCode'] = self.tag_code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.user_group is not None:
            result['UserGroup'] = self.user_group
        if self.device_group is not None:
            result['DeviceGroup'] = self.device_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TagCode') is not None:
            self.tag_code = m.get('TagCode')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('UserGroup') is not None:
            self.user_group = m.get('UserGroup')
        if m.get('DeviceGroup') is not None:
            self.device_group = m.get('DeviceGroup')
        return self


class ListCorpGroupMetricsResponseBodyData(TeaModel):
    def __init__(
        self,
        date_id: str = None,
        device_group_id: str = None,
        corp_group_id: str = None,
        device_id: str = None,
        user_group_id: str = None,
        tag_code: str = None,
        corp_id: str = None,
        tag_metrics: str = None,
        tag_value: str = None,
        person_id: str = None,
    ):
        self.date_id = date_id
        self.device_group_id = device_group_id
        self.corp_group_id = corp_group_id
        self.device_id = device_id
        self.user_group_id = user_group_id
        self.tag_code = tag_code
        self.corp_id = corp_id
        self.tag_metrics = tag_metrics
        self.tag_value = tag_value
        self.person_id = person_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_id is not None:
            result['DateId'] = self.date_id
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.corp_group_id is not None:
            result['CorpGroupId'] = self.corp_group_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.tag_code is not None:
            result['TagCode'] = self.tag_code
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.tag_metrics is not None:
            result['TagMetrics'] = self.tag_metrics
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.person_id is not None:
            result['PersonID'] = self.person_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateId') is not None:
            self.date_id = m.get('DateId')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('CorpGroupId') is not None:
            self.corp_group_id = m.get('CorpGroupId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('TagCode') is not None:
            self.tag_code = m.get('TagCode')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TagMetrics') is not None:
            self.tag_metrics = m.get('TagMetrics')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('PersonID') is not None:
            self.person_id = m.get('PersonID')
        return self


class ListCorpGroupMetricsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListCorpGroupMetricsResponseBodyData] = None,
        code: str = None,
        success: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListCorpGroupMetricsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCorpGroupMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListCorpGroupMetricsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListCorpGroupMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCorpGroupsRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.corp_id = corp_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListCorpGroupsResponseBodyData(TeaModel):
    def __init__(
        self,
        records: List[str] = None,
        total_page: int = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.records = records
        self.total_page = total_page
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.records is not None:
            result['Records'] = self.records
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Records') is not None:
            self.records = m.get('Records')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCorpGroupsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListCorpGroupsResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListCorpGroupsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListCorpGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListCorpGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListCorpGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCorpMetricsRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        tag_code: str = None,
        start_time: str = None,
        end_time: str = None,
        page_number: str = None,
        page_size: str = None,
        user_group_list: str = None,
        device_group_list: str = None,
        device_id_list: str = None,
    ):
        self.corp_id = corp_id
        self.tag_code = tag_code
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.user_group_list = user_group_list
        self.device_group_list = device_group_list
        self.device_id_list = device_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.tag_code is not None:
            result['TagCode'] = self.tag_code
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_group_list is not None:
            result['UserGroupList'] = self.user_group_list
        if self.device_group_list is not None:
            result['DeviceGroupList'] = self.device_group_list
        if self.device_id_list is not None:
            result['DeviceIdList'] = self.device_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TagCode') is not None:
            self.tag_code = m.get('TagCode')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserGroupList') is not None:
            self.user_group_list = m.get('UserGroupList')
        if m.get('DeviceGroupList') is not None:
            self.device_group_list = m.get('DeviceGroupList')
        if m.get('DeviceIdList') is not None:
            self.device_id_list = m.get('DeviceIdList')
        return self


class ListCorpMetricsResponseBodyData(TeaModel):
    def __init__(
        self,
        date_id: str = None,
        device_group_id: str = None,
        device_id: str = None,
        user_group_id: str = None,
        tag_code: str = None,
        corp_id: str = None,
        tag_metrics: str = None,
        tag_value: str = None,
        person_id: str = None,
    ):
        self.date_id = date_id
        self.device_group_id = device_group_id
        self.device_id = device_id
        self.user_group_id = user_group_id
        self.tag_code = tag_code
        self.corp_id = corp_id
        self.tag_metrics = tag_metrics
        self.tag_value = tag_value
        self.person_id = person_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_id is not None:
            result['DateId'] = self.date_id
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.tag_code is not None:
            result['TagCode'] = self.tag_code
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.tag_metrics is not None:
            result['TagMetrics'] = self.tag_metrics
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateId') is not None:
            self.date_id = m.get('DateId')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('TagCode') is not None:
            self.tag_code = m.get('TagCode')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TagMetrics') is not None:
            self.tag_metrics = m.get('TagMetrics')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        return self


class ListCorpMetricsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListCorpMetricsResponseBodyData] = None,
        code: str = None,
        success: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListCorpMetricsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCorpMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListCorpMetricsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListCorpMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCorpsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        corp_name: str = None,
    ):
        # 页码
        self.page_number = page_number
        # 分页大小
        self.page_size = page_size
        self.corp_name = corp_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.corp_name is not None:
            result['CorpName'] = self.corp_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CorpName') is not None:
            self.corp_name = m.get('CorpName')
        return self


class ListCorpsResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        parent_corp_id: str = None,
        app_name: str = None,
        isv_sub_id: str = None,
        description: str = None,
        corp_name: str = None,
        corp_id: str = None,
        acu_used: int = None,
        create_date: str = None,
        icon_path: str = None,
        device_count: int = None,
    ):
        self.parent_corp_id = parent_corp_id
        self.app_name = app_name
        self.isv_sub_id = isv_sub_id
        self.description = description
        self.corp_name = corp_name
        self.corp_id = corp_id
        self.acu_used = acu_used
        self.create_date = create_date
        self.icon_path = icon_path
        self.device_count = device_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_corp_id is not None:
            result['ParentCorpId'] = self.parent_corp_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.description is not None:
            result['Description'] = self.description
        if self.corp_name is not None:
            result['CorpName'] = self.corp_name
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.acu_used is not None:
            result['AcuUsed'] = self.acu_used
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.icon_path is not None:
            result['IconPath'] = self.icon_path
        if self.device_count is not None:
            result['DeviceCount'] = self.device_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParentCorpId') is not None:
            self.parent_corp_id = m.get('ParentCorpId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CorpName') is not None:
            self.corp_name = m.get('CorpName')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('AcuUsed') is not None:
            self.acu_used = m.get('AcuUsed')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('IconPath') is not None:
            self.icon_path = m.get('IconPath')
        if m.get('DeviceCount') is not None:
            self.device_count = m.get('DeviceCount')
        return self


class ListCorpsResponseBodyData(TeaModel):
    def __init__(
        self,
        records: List[ListCorpsResponseBodyDataRecords] = None,
        total_page: int = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.records = records
        self.total_page = total_page
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListCorpsResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCorpsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListCorpsResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListCorpsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListCorpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListCorpsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListCorpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceGroupsRequest(TeaModel):
    def __init__(
        self,
        device_code_list: str = None,
        corp_id_list: str = None,
        name: str = None,
        is_page: int = None,
        page_num: int = None,
        page_size: int = None,
        group: str = None,
        data_source_type: str = None,
    ):
        self.device_code_list = device_code_list
        self.corp_id_list = corp_id_list
        self.name = name
        self.is_page = is_page
        self.page_num = page_num
        self.page_size = page_size
        self.group = group
        self.data_source_type = data_source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_code_list is not None:
            result['DeviceCodeList'] = self.device_code_list
        if self.corp_id_list is not None:
            result['CorpIdList'] = self.corp_id_list
        if self.name is not None:
            result['Name'] = self.name
        if self.is_page is not None:
            result['IsPage'] = self.is_page
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.group is not None:
            result['Group'] = self.group
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceCodeList') is not None:
            self.device_code_list = m.get('DeviceCodeList')
        if m.get('CorpIdList') is not None:
            self.corp_id_list = m.get('CorpIdList')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('IsPage') is not None:
            self.is_page = m.get('IsPage')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        return self


class ListDeviceGroupsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        device_stream_status: str = None,
        device_name: str = None,
        device_status: str = None,
        region_id: str = None,
        device_sn: str = None,
        device_compute_status: str = None,
        install_address: str = None,
        device_group: str = None,
        region_name: str = None,
        data_source_type: str = None,
        resolving_power: str = None,
        device_code: str = None,
        bit_rate: str = None,
        coding_format: str = None,
        type: str = None,
    ):
        self.device_stream_status = device_stream_status
        self.device_name = device_name
        self.device_status = device_status
        self.region_id = region_id
        self.device_sn = device_sn
        self.device_compute_status = device_compute_status
        self.install_address = install_address
        self.device_group = device_group
        self.region_name = region_name
        self.data_source_type = data_source_type
        self.resolving_power = resolving_power
        self.device_code = device_code
        self.bit_rate = bit_rate
        self.coding_format = coding_format
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_stream_status is not None:
            result['DeviceStreamStatus'] = self.device_stream_status
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.device_compute_status is not None:
            result['DeviceComputeStatus'] = self.device_compute_status
        if self.install_address is not None:
            result['InstallAddress'] = self.install_address
        if self.device_group is not None:
            result['DeviceGroup'] = self.device_group
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.resolving_power is not None:
            result['ResolvingPower'] = self.resolving_power
        if self.device_code is not None:
            result['DeviceCode'] = self.device_code
        if self.bit_rate is not None:
            result['BitRate'] = self.bit_rate
        if self.coding_format is not None:
            result['CodingFormat'] = self.coding_format
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceStreamStatus') is not None:
            self.device_stream_status = m.get('DeviceStreamStatus')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('DeviceComputeStatus') is not None:
            self.device_compute_status = m.get('DeviceComputeStatus')
        if m.get('InstallAddress') is not None:
            self.install_address = m.get('InstallAddress')
        if m.get('DeviceGroup') is not None:
            self.device_group = m.get('DeviceGroup')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('ResolvingPower') is not None:
            self.resolving_power = m.get('ResolvingPower')
        if m.get('DeviceCode') is not None:
            self.device_code = m.get('DeviceCode')
        if m.get('BitRate') is not None:
            self.bit_rate = m.get('BitRate')
        if m.get('CodingFormat') is not None:
            self.coding_format = m.get('CodingFormat')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListDeviceGroupsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListDeviceGroupsResponseBodyDataList] = None,
        total_count: str = None,
    ):
        self.list = list
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListDeviceGroupsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDeviceGroupsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[ListDeviceGroupsResponseBodyData] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListDeviceGroupsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListDeviceGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDeviceGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDeviceGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDevicesRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        gb_id: str = None,
        device_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.corp_id = corp_id
        self.gb_id = gb_id
        self.device_name = device_name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListDevicesResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        status: int = None,
        sip_gbid: str = None,
        device_direction: str = None,
        device_name: str = None,
        device_address: str = None,
        device_type: str = None,
        create_time: str = None,
        sip_password: str = None,
        sip_server_port: str = None,
        vendor: str = None,
        gb_id: str = None,
        cover_image_url: str = None,
        access_protocol_type: str = None,
        device_site: str = None,
        longitude: str = None,
        latitude: str = None,
        resolution: str = None,
        sip_server_ip: str = None,
        bit_rate: str = None,
    ):
        self.status = status
        self.sip_gbid = sip_gbid
        self.device_direction = device_direction
        self.device_name = device_name
        self.device_address = device_address
        self.device_type = device_type
        self.create_time = create_time
        self.sip_password = sip_password
        self.sip_server_port = sip_server_port
        self.vendor = vendor
        self.gb_id = gb_id
        self.cover_image_url = cover_image_url
        self.access_protocol_type = access_protocol_type
        self.device_site = device_site
        self.longitude = longitude
        self.latitude = latitude
        self.resolution = resolution
        self.sip_server_ip = sip_server_ip
        self.bit_rate = bit_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.sip_gbid is not None:
            result['SipGBId'] = self.sip_gbid
        if self.device_direction is not None:
            result['DeviceDirection'] = self.device_direction
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_address is not None:
            result['DeviceAddress'] = self.device_address
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.sip_password is not None:
            result['SipPassword'] = self.sip_password
        if self.sip_server_port is not None:
            result['SipServerPort'] = self.sip_server_port
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.cover_image_url is not None:
            result['CoverImageUrl'] = self.cover_image_url
        if self.access_protocol_type is not None:
            result['AccessProtocolType'] = self.access_protocol_type
        if self.device_site is not None:
            result['DeviceSite'] = self.device_site
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.sip_server_ip is not None:
            result['SipServerIp'] = self.sip_server_ip
        if self.bit_rate is not None:
            result['BitRate'] = self.bit_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SipGBId') is not None:
            self.sip_gbid = m.get('SipGBId')
        if m.get('DeviceDirection') is not None:
            self.device_direction = m.get('DeviceDirection')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceAddress') is not None:
            self.device_address = m.get('DeviceAddress')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SipPassword') is not None:
            self.sip_password = m.get('SipPassword')
        if m.get('SipServerPort') is not None:
            self.sip_server_port = m.get('SipServerPort')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('CoverImageUrl') is not None:
            self.cover_image_url = m.get('CoverImageUrl')
        if m.get('AccessProtocolType') is not None:
            self.access_protocol_type = m.get('AccessProtocolType')
        if m.get('DeviceSite') is not None:
            self.device_site = m.get('DeviceSite')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('SipServerIp') is not None:
            self.sip_server_ip = m.get('SipServerIp')
        if m.get('BitRate') is not None:
            self.bit_rate = m.get('BitRate')
        return self


class ListDevicesResponseBodyData(TeaModel):
    def __init__(
        self,
        records: List[ListDevicesResponseBodyDataRecords] = None,
        total_page: int = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.records = records
        self.total_page = total_page
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListDevicesResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDevicesResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListDevicesResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListDevicesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDevicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEventAlgorithmDetailsRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        event_type: str = None,
        data_source_id: str = None,
        start_time: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        source_id: str = None,
        record_id: str = None,
        event_value: str = None,
        extend_value: str = None,
    ):
        self.corp_id = corp_id
        self.event_type = event_type
        self.data_source_id = data_source_id
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.source_id = source_id
        self.record_id = record_id
        self.event_value = event_value
        self.extend_value = extend_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.event_value is not None:
            result['EventValue'] = self.event_value
        if self.extend_value is not None:
            result['ExtendValue'] = self.extend_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('EventValue') is not None:
            self.event_value = m.get('EventValue')
        if m.get('ExtendValue') is not None:
            self.extend_value = m.get('ExtendValue')
        return self


class ListEventAlgorithmDetailsResponseBodyData(TeaModel):
    def __init__(
        self,
        right_bottom_y: str = None,
        data_source_id: str = None,
        pic_url_path: str = None,
        record_id: str = None,
        extend_value: str = None,
        face_count: str = None,
        right_bottom_x: str = None,
        source_id: str = None,
        extra_extend_value: str = None,
        target_pic_url_path: str = None,
        event_type: str = None,
        point_y: str = None,
        left_top_y: str = None,
        point_x: str = None,
        corp_id: str = None,
        event_value: str = None,
        shot_time: str = None,
        left_top_x: str = None,
        tag_code: str = None,
        tag_code_reliability: str = None,
        uuid_code: str = None,
    ):
        self.right_bottom_y = right_bottom_y
        self.data_source_id = data_source_id
        self.pic_url_path = pic_url_path
        self.record_id = record_id
        self.extend_value = extend_value
        self.face_count = face_count
        self.right_bottom_x = right_bottom_x
        self.source_id = source_id
        self.extra_extend_value = extra_extend_value
        self.target_pic_url_path = target_pic_url_path
        self.event_type = event_type
        self.point_y = point_y
        self.left_top_y = left_top_y
        self.point_x = point_x
        self.corp_id = corp_id
        self.event_value = event_value
        self.shot_time = shot_time
        self.left_top_x = left_top_x
        self.tag_code = tag_code
        self.tag_code_reliability = tag_code_reliability
        self.uuid_code = uuid_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.right_bottom_y is not None:
            result['RightBottomY'] = self.right_bottom_y
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.pic_url_path is not None:
            result['PicUrlPath'] = self.pic_url_path
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.extend_value is not None:
            result['ExtendValue'] = self.extend_value
        if self.face_count is not None:
            result['FaceCount'] = self.face_count
        if self.right_bottom_x is not None:
            result['RightBottomX'] = self.right_bottom_x
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.extra_extend_value is not None:
            result['ExtraExtendValue'] = self.extra_extend_value
        if self.target_pic_url_path is not None:
            result['TargetPicUrlPath'] = self.target_pic_url_path
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.point_y is not None:
            result['PointY'] = self.point_y
        if self.left_top_y is not None:
            result['LeftTopY'] = self.left_top_y
        if self.point_x is not None:
            result['PointX'] = self.point_x
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.event_value is not None:
            result['EventValue'] = self.event_value
        if self.shot_time is not None:
            result['ShotTime'] = self.shot_time
        if self.left_top_x is not None:
            result['LeftTopX'] = self.left_top_x
        if self.tag_code is not None:
            result['TagCode'] = self.tag_code
        if self.tag_code_reliability is not None:
            result['TagCodeReliability'] = self.tag_code_reliability
        if self.uuid_code is not None:
            result['UuidCode'] = self.uuid_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RightBottomY') is not None:
            self.right_bottom_y = m.get('RightBottomY')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('PicUrlPath') is not None:
            self.pic_url_path = m.get('PicUrlPath')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('ExtendValue') is not None:
            self.extend_value = m.get('ExtendValue')
        if m.get('FaceCount') is not None:
            self.face_count = m.get('FaceCount')
        if m.get('RightBottomX') is not None:
            self.right_bottom_x = m.get('RightBottomX')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('ExtraExtendValue') is not None:
            self.extra_extend_value = m.get('ExtraExtendValue')
        if m.get('TargetPicUrlPath') is not None:
            self.target_pic_url_path = m.get('TargetPicUrlPath')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('PointY') is not None:
            self.point_y = m.get('PointY')
        if m.get('LeftTopY') is not None:
            self.left_top_y = m.get('LeftTopY')
        if m.get('PointX') is not None:
            self.point_x = m.get('PointX')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('EventValue') is not None:
            self.event_value = m.get('EventValue')
        if m.get('ShotTime') is not None:
            self.shot_time = m.get('ShotTime')
        if m.get('LeftTopX') is not None:
            self.left_top_x = m.get('LeftTopX')
        if m.get('TagCode') is not None:
            self.tag_code = m.get('TagCode')
        if m.get('TagCodeReliability') is not None:
            self.tag_code_reliability = m.get('TagCodeReliability')
        if m.get('UuidCode') is not None:
            self.uuid_code = m.get('UuidCode')
        return self


class ListEventAlgorithmDetailsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListEventAlgorithmDetailsResponseBodyData] = None,
        code: str = None,
        success: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListEventAlgorithmDetailsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListEventAlgorithmDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEventAlgorithmDetailsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEventAlgorithmDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEventAlgorithmResultsRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        event_type: str = None,
        data_source_id: str = None,
        start_time: str = None,
        end_time: str = None,
        page_number: str = None,
        page_size: str = None,
        extend_value: str = None,
    ):
        self.corp_id = corp_id
        self.event_type = event_type
        self.data_source_id = data_source_id
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.extend_value = extend_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.extend_value is not None:
            result['ExtendValue'] = self.extend_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ExtendValue') is not None:
            self.extend_value = m.get('ExtendValue')
        return self


class ListEventAlgorithmResultsResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        extend_value_two: str = None,
        record_id: str = None,
        pic_url_path: str = None,
        data_source_id: str = None,
        extend_value: str = None,
        extend_value_three: str = None,
        face_count: str = None,
        target_pic_url_path: str = None,
        event_type: str = None,
        corp_id: str = None,
        shot_time: str = None,
        cap_style: str = None,
        tag_code: str = None,
        tag_code_reliability: str = None,
        uuid_code: str = None,
    ):
        self.extend_value_two = extend_value_two
        self.record_id = record_id
        self.pic_url_path = pic_url_path
        self.data_source_id = data_source_id
        self.extend_value = extend_value
        self.extend_value_three = extend_value_three
        self.face_count = face_count
        self.target_pic_url_path = target_pic_url_path
        self.event_type = event_type
        self.corp_id = corp_id
        self.shot_time = shot_time
        self.cap_style = cap_style
        self.tag_code = tag_code
        self.tag_code_reliability = tag_code_reliability
        self.uuid_code = uuid_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend_value_two is not None:
            result['ExtendValueTwo'] = self.extend_value_two
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.pic_url_path is not None:
            result['PicUrlPath'] = self.pic_url_path
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.extend_value is not None:
            result['ExtendValue'] = self.extend_value
        if self.extend_value_three is not None:
            result['ExtendValueThree'] = self.extend_value_three
        if self.face_count is not None:
            result['FaceCount'] = self.face_count
        if self.target_pic_url_path is not None:
            result['TargetPicUrlPath'] = self.target_pic_url_path
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.shot_time is not None:
            result['ShotTime'] = self.shot_time
        if self.cap_style is not None:
            result['CapStyle'] = self.cap_style
        if self.tag_code is not None:
            result['TagCode'] = self.tag_code
        if self.tag_code_reliability is not None:
            result['TagCodeReliability'] = self.tag_code_reliability
        if self.uuid_code is not None:
            result['UuidCode'] = self.uuid_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendValueTwo') is not None:
            self.extend_value_two = m.get('ExtendValueTwo')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('PicUrlPath') is not None:
            self.pic_url_path = m.get('PicUrlPath')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('ExtendValue') is not None:
            self.extend_value = m.get('ExtendValue')
        if m.get('ExtendValueThree') is not None:
            self.extend_value_three = m.get('ExtendValueThree')
        if m.get('FaceCount') is not None:
            self.face_count = m.get('FaceCount')
        if m.get('TargetPicUrlPath') is not None:
            self.target_pic_url_path = m.get('TargetPicUrlPath')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('ShotTime') is not None:
            self.shot_time = m.get('ShotTime')
        if m.get('CapStyle') is not None:
            self.cap_style = m.get('CapStyle')
        if m.get('TagCode') is not None:
            self.tag_code = m.get('TagCode')
        if m.get('TagCodeReliability') is not None:
            self.tag_code_reliability = m.get('TagCodeReliability')
        if m.get('UuidCode') is not None:
            self.uuid_code = m.get('UuidCode')
        return self


class ListEventAlgorithmResultsResponseBodyData(TeaModel):
    def __init__(
        self,
        records: List[ListEventAlgorithmResultsResponseBodyDataRecords] = None,
        total_page: int = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.records = records
        self.total_page = total_page
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListEventAlgorithmResultsResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEventAlgorithmResultsResponseBody(TeaModel):
    def __init__(
        self,
        extend_value: str = None,
        message: str = None,
        request_id: str = None,
        data: ListEventAlgorithmResultsResponseBodyData = None,
        code: str = None,
    ):
        self.extend_value = extend_value
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend_value is not None:
            result['ExtendValue'] = self.extend_value
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendValue') is not None:
            self.extend_value = m.get('ExtendValue')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListEventAlgorithmResultsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListEventAlgorithmResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEventAlgorithmResultsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEventAlgorithmResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFaceAlgorithmResultsRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        algorithm_type: str = None,
        data_source_id: str = None,
        start_time: str = None,
        end_time: str = None,
        page_number: str = None,
        page_size: str = None,
    ):
        self.corp_id = corp_id
        self.algorithm_type = algorithm_type
        self.data_source_id = data_source_id
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.algorithm_type is not None:
            result['AlgorithmType'] = self.algorithm_type
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('AlgorithmType') is not None:
            self.algorithm_type = m.get('AlgorithmType')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListFaceAlgorithmResultsResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        right_bottom_y: float = None,
        data_source_id: str = None,
        pic_url_path: str = None,
        face_id: str = None,
        right_bottom_x: float = None,
        source_id: str = None,
        max_age: str = None,
        target_pic_url_path: str = None,
        hair_style: str = None,
        left_top_y: float = None,
        min_age: str = None,
        corp_id: str = None,
        shot_time: str = None,
        gender_code: str = None,
        cap_style: str = None,
        left_top_x: float = None,
    ):
        self.right_bottom_y = right_bottom_y
        self.data_source_id = data_source_id
        self.pic_url_path = pic_url_path
        self.face_id = face_id
        self.right_bottom_x = right_bottom_x
        self.source_id = source_id
        self.max_age = max_age
        self.target_pic_url_path = target_pic_url_path
        self.hair_style = hair_style
        self.left_top_y = left_top_y
        self.min_age = min_age
        self.corp_id = corp_id
        self.shot_time = shot_time
        self.gender_code = gender_code
        self.cap_style = cap_style
        self.left_top_x = left_top_x

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.right_bottom_y is not None:
            result['RightBottomY'] = self.right_bottom_y
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.pic_url_path is not None:
            result['PicUrlPath'] = self.pic_url_path
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.right_bottom_x is not None:
            result['RightBottomX'] = self.right_bottom_x
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.max_age is not None:
            result['MaxAge'] = self.max_age
        if self.target_pic_url_path is not None:
            result['TargetPicUrlPath'] = self.target_pic_url_path
        if self.hair_style is not None:
            result['HairStyle'] = self.hair_style
        if self.left_top_y is not None:
            result['LeftTopY'] = self.left_top_y
        if self.min_age is not None:
            result['MinAge'] = self.min_age
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.shot_time is not None:
            result['ShotTime'] = self.shot_time
        if self.gender_code is not None:
            result['GenderCode'] = self.gender_code
        if self.cap_style is not None:
            result['CapStyle'] = self.cap_style
        if self.left_top_x is not None:
            result['LeftTopX'] = self.left_top_x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RightBottomY') is not None:
            self.right_bottom_y = m.get('RightBottomY')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('PicUrlPath') is not None:
            self.pic_url_path = m.get('PicUrlPath')
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('RightBottomX') is not None:
            self.right_bottom_x = m.get('RightBottomX')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('MaxAge') is not None:
            self.max_age = m.get('MaxAge')
        if m.get('TargetPicUrlPath') is not None:
            self.target_pic_url_path = m.get('TargetPicUrlPath')
        if m.get('HairStyle') is not None:
            self.hair_style = m.get('HairStyle')
        if m.get('LeftTopY') is not None:
            self.left_top_y = m.get('LeftTopY')
        if m.get('MinAge') is not None:
            self.min_age = m.get('MinAge')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('ShotTime') is not None:
            self.shot_time = m.get('ShotTime')
        if m.get('GenderCode') is not None:
            self.gender_code = m.get('GenderCode')
        if m.get('CapStyle') is not None:
            self.cap_style = m.get('CapStyle')
        if m.get('LeftTopX') is not None:
            self.left_top_x = m.get('LeftTopX')
        return self


class ListFaceAlgorithmResultsResponseBodyData(TeaModel):
    def __init__(
        self,
        records: List[ListFaceAlgorithmResultsResponseBodyDataRecords] = None,
        total_page: int = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.records = records
        self.total_page = total_page
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListFaceAlgorithmResultsResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFaceAlgorithmResultsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListFaceAlgorithmResultsResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListFaceAlgorithmResultsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListFaceAlgorithmResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFaceAlgorithmResultsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFaceAlgorithmResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMarkerRequest(TeaModel):
    def __init__(
        self,
        algorithm_id: str = None,
        sample_id: str = None,
        page_size: str = None,
        page_num: str = None,
    ):
        self.algorithm_id = algorithm_id
        self.sample_id = sample_id
        self.page_size = page_size
        self.page_num = page_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.sample_id is not None:
            result['SampleId'] = self.sample_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('SampleId') is not None:
            self.sample_id = m.get('SampleId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        return self


class ListMarkerResponseBodyDataList(TeaModel):
    def __init__(
        self,
        id: str = None,
        algorithm_id: str = None,
        user_id: str = None,
        label_id: str = None,
        label_name: str = None,
        sample_id: str = None,
        content: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
    ):
        self.id = id
        self.algorithm_id = algorithm_id
        self.user_id = user_id
        self.label_id = label_id
        self.label_name = label_name
        self.sample_id = sample_id
        self.content = content
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        if self.label_name is not None:
            result['LabelName'] = self.label_name
        if self.sample_id is not None:
            result['SampleId'] = self.sample_id
        if self.content is not None:
            result['Content'] = self.content
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        if m.get('LabelName') is not None:
            self.label_name = m.get('LabelName')
        if m.get('SampleId') is not None:
            self.sample_id = m.get('SampleId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        return self


class ListMarkerResponseBodyData(TeaModel):
    def __init__(
        self,
        total: int = None,
        list: List[ListMarkerResponseBodyDataList] = None,
    ):
        self.total = total
        self.list = list

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total is not None:
            result['Total'] = self.total
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListMarkerResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        return self


class ListMarkerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        data: ListMarkerResponseBodyData = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.message = message
        self.code = code
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListMarkerResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListMarkerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListMarkerResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListMarkerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMetricsRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        tag_code: str = None,
        aggregate_type: str = None,
        start_time: str = None,
        end_time: str = None,
        page_number: str = None,
        page_size: str = None,
    ):
        self.corp_id = corp_id
        self.tag_code = tag_code
        self.aggregate_type = aggregate_type
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.tag_code is not None:
            result['TagCode'] = self.tag_code
        if self.aggregate_type is not None:
            result['AggregateType'] = self.aggregate_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TagCode') is not None:
            self.tag_code = m.get('TagCode')
        if m.get('AggregateType') is not None:
            self.aggregate_type = m.get('AggregateType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListMetricsResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        tag_metric: str = None,
        tag_code: str = None,
        tag_value: str = None,
        date_time: str = None,
    ):
        self.tag_metric = tag_metric
        self.tag_code = tag_code
        self.tag_value = tag_value
        self.date_time = date_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_metric is not None:
            result['TagMetric'] = self.tag_metric
        if self.tag_code is not None:
            result['TagCode'] = self.tag_code
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.date_time is not None:
            result['DateTime'] = self.date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagMetric') is not None:
            self.tag_metric = m.get('TagMetric')
        if m.get('TagCode') is not None:
            self.tag_code = m.get('TagCode')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('DateTime') is not None:
            self.date_time = m.get('DateTime')
        return self


class ListMetricsResponseBodyData(TeaModel):
    def __init__(
        self,
        records: List[ListMetricsResponseBodyDataRecords] = None,
        total_page: int = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.records = records
        self.total_page = total_page
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListMetricsResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListMetricsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListMetricsResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListMetricsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListMetricsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMotorAlgorithmResultsRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        algorithm_type: str = None,
        data_source_id: str = None,
        start_time: str = None,
        end_time: str = None,
        page_number: str = None,
        page_size: str = None,
        plate_number: str = None,
    ):
        self.corp_id = corp_id
        self.algorithm_type = algorithm_type
        self.data_source_id = data_source_id
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.plate_number = plate_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.algorithm_type is not None:
            result['AlgorithmType'] = self.algorithm_type
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.plate_number is not None:
            result['PlateNumber'] = self.plate_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('AlgorithmType') is not None:
            self.algorithm_type = m.get('AlgorithmType')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlateNumber') is not None:
            self.plate_number = m.get('PlateNumber')
        return self


class ListMotorAlgorithmResultsResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        motor_class: str = None,
        right_bottom_y: float = None,
        data_source_id: str = None,
        pic_url_path: str = None,
        plate_class: str = None,
        plate_color: str = None,
        right_bottom_x: float = None,
        source_id: str = None,
        safety_belt: str = None,
        motor_style: str = None,
        target_pic_url_path: str = None,
        left_top_y: float = None,
        motor_color: str = None,
        plate_number: str = None,
        corp_id: str = None,
        shot_time: str = None,
        calling: str = None,
        left_top_x: float = None,
        motor_brand: str = None,
        motor_model: str = None,
        motor_id: str = None,
    ):
        self.motor_class = motor_class
        self.right_bottom_y = right_bottom_y
        self.data_source_id = data_source_id
        self.pic_url_path = pic_url_path
        self.plate_class = plate_class
        self.plate_color = plate_color
        self.right_bottom_x = right_bottom_x
        self.source_id = source_id
        self.safety_belt = safety_belt
        self.motor_style = motor_style
        self.target_pic_url_path = target_pic_url_path
        self.left_top_y = left_top_y
        self.motor_color = motor_color
        self.plate_number = plate_number
        self.corp_id = corp_id
        self.shot_time = shot_time
        self.calling = calling
        self.left_top_x = left_top_x
        self.motor_brand = motor_brand
        self.motor_model = motor_model
        self.motor_id = motor_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.motor_class is not None:
            result['MotorClass'] = self.motor_class
        if self.right_bottom_y is not None:
            result['RightBottomY'] = self.right_bottom_y
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.pic_url_path is not None:
            result['PicUrlPath'] = self.pic_url_path
        if self.plate_class is not None:
            result['PlateClass'] = self.plate_class
        if self.plate_color is not None:
            result['PlateColor'] = self.plate_color
        if self.right_bottom_x is not None:
            result['RightBottomX'] = self.right_bottom_x
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.safety_belt is not None:
            result['SafetyBelt'] = self.safety_belt
        if self.motor_style is not None:
            result['MotorStyle'] = self.motor_style
        if self.target_pic_url_path is not None:
            result['TargetPicUrlPath'] = self.target_pic_url_path
        if self.left_top_y is not None:
            result['LeftTopY'] = self.left_top_y
        if self.motor_color is not None:
            result['MotorColor'] = self.motor_color
        if self.plate_number is not None:
            result['PlateNumber'] = self.plate_number
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.shot_time is not None:
            result['ShotTime'] = self.shot_time
        if self.calling is not None:
            result['Calling'] = self.calling
        if self.left_top_x is not None:
            result['LeftTopX'] = self.left_top_x
        if self.motor_brand is not None:
            result['MotorBrand'] = self.motor_brand
        if self.motor_model is not None:
            result['MotorModel'] = self.motor_model
        if self.motor_id is not None:
            result['MotorId'] = self.motor_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MotorClass') is not None:
            self.motor_class = m.get('MotorClass')
        if m.get('RightBottomY') is not None:
            self.right_bottom_y = m.get('RightBottomY')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('PicUrlPath') is not None:
            self.pic_url_path = m.get('PicUrlPath')
        if m.get('PlateClass') is not None:
            self.plate_class = m.get('PlateClass')
        if m.get('PlateColor') is not None:
            self.plate_color = m.get('PlateColor')
        if m.get('RightBottomX') is not None:
            self.right_bottom_x = m.get('RightBottomX')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SafetyBelt') is not None:
            self.safety_belt = m.get('SafetyBelt')
        if m.get('MotorStyle') is not None:
            self.motor_style = m.get('MotorStyle')
        if m.get('TargetPicUrlPath') is not None:
            self.target_pic_url_path = m.get('TargetPicUrlPath')
        if m.get('LeftTopY') is not None:
            self.left_top_y = m.get('LeftTopY')
        if m.get('MotorColor') is not None:
            self.motor_color = m.get('MotorColor')
        if m.get('PlateNumber') is not None:
            self.plate_number = m.get('PlateNumber')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('ShotTime') is not None:
            self.shot_time = m.get('ShotTime')
        if m.get('Calling') is not None:
            self.calling = m.get('Calling')
        if m.get('LeftTopX') is not None:
            self.left_top_x = m.get('LeftTopX')
        if m.get('MotorBrand') is not None:
            self.motor_brand = m.get('MotorBrand')
        if m.get('MotorModel') is not None:
            self.motor_model = m.get('MotorModel')
        if m.get('MotorId') is not None:
            self.motor_id = m.get('MotorId')
        return self


class ListMotorAlgorithmResultsResponseBodyData(TeaModel):
    def __init__(
        self,
        records: List[ListMotorAlgorithmResultsResponseBodyDataRecords] = None,
        total_page: int = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.records = records
        self.total_page = total_page
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListMotorAlgorithmResultsResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListMotorAlgorithmResultsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListMotorAlgorithmResultsResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListMotorAlgorithmResultsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListMotorAlgorithmResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListMotorAlgorithmResultsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListMotorAlgorithmResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNVRChannelDeviceRequest(TeaModel):
    def __init__(
        self,
        device_code: str = None,
        is_page: str = None,
        page_num: str = None,
        page_size: str = None,
    ):
        self.device_code = device_code
        self.is_page = is_page
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_code is not None:
            result['DeviceCode'] = self.device_code
        if self.is_page is not None:
            result['IsPage'] = self.is_page
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceCode') is not None:
            self.device_code = m.get('DeviceCode')
        if m.get('IsPage') is not None:
            self.is_page = m.get('IsPage')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListNVRChannelDeviceResponseBodyData(TeaModel):
    def __init__(
        self,
        device_code: str = None,
        device_name: str = None,
        device_type: str = None,
        datasource_type: str = None,
        device_status: str = None,
        stream_status: str = None,
        compture_status: str = None,
        device_sn: str = None,
        sample_name: str = None,
        region_name: str = None,
        corp_id: str = None,
        vap: str = None,
        project_name: str = None,
    ):
        self.device_code = device_code
        self.device_name = device_name
        self.device_type = device_type
        self.datasource_type = datasource_type
        self.device_status = device_status
        self.stream_status = stream_status
        self.compture_status = compture_status
        self.device_sn = device_sn
        self.sample_name = sample_name
        self.region_name = region_name
        self.corp_id = corp_id
        self.vap = vap
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_code is not None:
            result['DeviceCode'] = self.device_code
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.datasource_type is not None:
            result['DatasourceType'] = self.datasource_type
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status
        if self.stream_status is not None:
            result['StreamStatus'] = self.stream_status
        if self.compture_status is not None:
            result['ComptureStatus'] = self.compture_status
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.sample_name is not None:
            result['SampleName'] = self.sample_name
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.vap is not None:
            result['Vap'] = self.vap
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceCode') is not None:
            self.device_code = m.get('DeviceCode')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('DatasourceType') is not None:
            self.datasource_type = m.get('DatasourceType')
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')
        if m.get('StreamStatus') is not None:
            self.stream_status = m.get('StreamStatus')
        if m.get('ComptureStatus') is not None:
            self.compture_status = m.get('ComptureStatus')
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('SampleName') is not None:
            self.sample_name = m.get('SampleName')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('Vap') is not None:
            self.vap = m.get('Vap')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class ListNVRChannelDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        total: str = None,
        data: List[ListNVRChannelDeviceResponseBodyData] = None,
        message: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.total = total
        self.data = data
        self.message = message

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListNVRChannelDeviceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ListNVRChannelDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListNVRChannelDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListNVRChannelDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNVRDeviceRequest(TeaModel):
    def __init__(
        self,
        device_code: str = None,
        corp_id_list: str = None,
        is_page: int = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.device_code = device_code
        self.corp_id_list = corp_id_list
        self.is_page = is_page
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_code is not None:
            result['DeviceCode'] = self.device_code
        if self.corp_id_list is not None:
            result['CorpIdList'] = self.corp_id_list
        if self.is_page is not None:
            result['IsPage'] = self.is_page
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceCode') is not None:
            self.device_code = m.get('DeviceCode')
        if m.get('CorpIdList') is not None:
            self.corp_id_list = m.get('CorpIdList')
        if m.get('IsPage') is not None:
            self.is_page = m.get('IsPage')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListNVRDeviceResponseBodyData(TeaModel):
    def __init__(
        self,
        device_code: str = None,
        device_name: str = None,
        device_type: str = None,
        datasource_type: str = None,
        device_status: str = None,
        stream_status: str = None,
        compture_status: str = None,
        region_name: str = None,
        project_name: str = None,
        registration_time: str = None,
        access_quota: str = None,
        channel: str = None,
        device_sn: str = None,
        type: str = None,
        corp_id: str = None,
    ):
        self.device_code = device_code
        self.device_name = device_name
        self.device_type = device_type
        self.datasource_type = datasource_type
        self.device_status = device_status
        self.stream_status = stream_status
        self.compture_status = compture_status
        self.region_name = region_name
        self.project_name = project_name
        self.registration_time = registration_time
        self.access_quota = access_quota
        self.channel = channel
        self.device_sn = device_sn
        self.type = type
        self.corp_id = corp_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_code is not None:
            result['DeviceCode'] = self.device_code
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.datasource_type is not None:
            result['DatasourceType'] = self.datasource_type
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status
        if self.stream_status is not None:
            result['StreamStatus'] = self.stream_status
        if self.compture_status is not None:
            result['ComptureStatus'] = self.compture_status
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.registration_time is not None:
            result['RegistrationTime'] = self.registration_time
        if self.access_quota is not None:
            result['AccessQuota'] = self.access_quota
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.type is not None:
            result['Type'] = self.type
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceCode') is not None:
            self.device_code = m.get('DeviceCode')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('DatasourceType') is not None:
            self.datasource_type = m.get('DatasourceType')
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')
        if m.get('StreamStatus') is not None:
            self.stream_status = m.get('StreamStatus')
        if m.get('ComptureStatus') is not None:
            self.compture_status = m.get('ComptureStatus')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RegistrationTime') is not None:
            self.registration_time = m.get('RegistrationTime')
        if m.get('AccessQuota') is not None:
            self.access_quota = m.get('AccessQuota')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        return self


class ListNVRDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        total: str = None,
        data: List[ListNVRDeviceResponseBodyData] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.total = total
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListNVRDeviceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class ListNVRDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListNVRDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListNVRDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPersonsRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        page_no: str = None,
        page_size: str = None,
        start_time: str = None,
        end_time: str = None,
        algorithm_type: str = None,
    ):
        self.corp_id = corp_id
        self.page_no = page_no
        self.page_size = page_size
        self.start_time = start_time
        self.end_time = end_time
        self.algorithm_type = algorithm_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.algorithm_type is not None:
            result['AlgorithmType'] = self.algorithm_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('AlgorithmType') is not None:
            self.algorithm_type = m.get('AlgorithmType')
        return self


class ListPersonsResponseBodyDataRecordsTagList(TeaModel):
    def __init__(
        self,
        tag_value_id: str = None,
        tag_name: str = None,
        tag_code: str = None,
        tag_value: str = None,
    ):
        self.tag_value_id = tag_value_id
        self.tag_name = tag_name
        self.tag_code = tag_code
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_value_id is not None:
            result['TagValueId'] = self.tag_value_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.tag_code is not None:
            result['TagCode'] = self.tag_code
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagValueId') is not None:
            self.tag_value_id = m.get('TagValueId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TagCode') is not None:
            self.tag_code = m.get('TagCode')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListPersonsResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        pic_url: str = None,
        tag_list: List[ListPersonsResponseBodyDataRecordsTagList] = None,
        first_appear_time: str = None,
        person_id: str = None,
    ):
        self.pic_url = pic_url
        self.tag_list = tag_list
        self.first_appear_time = first_appear_time
        self.person_id = person_id

    def validate(self):
        if self.tag_list:
            for k in self.tag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        result['TagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['TagList'].append(k.to_map() if k else None)
        if self.first_appear_time is not None:
            result['FirstAppearTime'] = self.first_appear_time
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        self.tag_list = []
        if m.get('TagList') is not None:
            for k in m.get('TagList'):
                temp_model = ListPersonsResponseBodyDataRecordsTagList()
                self.tag_list.append(temp_model.from_map(k))
        if m.get('FirstAppearTime') is not None:
            self.first_appear_time = m.get('FirstAppearTime')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        return self


class ListPersonsResponseBodyData(TeaModel):
    def __init__(
        self,
        records: List[ListPersonsResponseBodyDataRecords] = None,
        page_no: str = None,
        total_page: str = None,
        page_size: str = None,
        total_count: str = None,
    ):
        self.records = records
        self.page_no = page_no
        self.total_page = total_page
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListPersonsResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPersonsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListPersonsResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListPersonsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListPersonsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPersonsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListPersonsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPersonTraceRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        corp_id: str = None,
        page_number: str = None,
        page_size: str = None,
        end_time: str = None,
        data_source_id: str = None,
        person_id: str = None,
        group_id: str = None,
    ):
        self.start_time = start_time
        self.corp_id = corp_id
        self.page_number = page_number
        self.page_size = page_size
        self.end_time = end_time
        self.data_source_id = data_source_id
        self.person_id = person_id
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class ListPersonTraceResponseBodyData(TeaModel):
    def __init__(
        self,
        end_target_image: str = None,
        last_time: str = None,
        start_time: str = None,
        group_id: str = None,
        device_id: str = None,
        end_source_image: str = None,
        corp_id: str = None,
        start_source_image: str = None,
        date: str = None,
        person_id: str = None,
        start_target_image: str = None,
    ):
        self.end_target_image = end_target_image
        self.last_time = last_time
        self.start_time = start_time
        self.group_id = group_id
        self.device_id = device_id
        self.end_source_image = end_source_image
        self.corp_id = corp_id
        self.start_source_image = start_source_image
        self.date = date
        self.person_id = person_id
        self.start_target_image = start_target_image

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_target_image is not None:
            result['EndTargetImage'] = self.end_target_image
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.end_source_image is not None:
            result['EndSourceImage'] = self.end_source_image
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.start_source_image is not None:
            result['StartSourceImage'] = self.start_source_image
        if self.date is not None:
            result['Date'] = self.date
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.start_target_image is not None:
            result['StartTargetImage'] = self.start_target_image
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTargetImage') is not None:
            self.end_target_image = m.get('EndTargetImage')
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('EndSourceImage') is not None:
            self.end_source_image = m.get('EndSourceImage')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('StartSourceImage') is not None:
            self.start_source_image = m.get('StartSourceImage')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('StartTargetImage') is not None:
            self.start_target_image = m.get('StartTargetImage')
        return self


class ListPersonTraceResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListPersonTraceResponseBodyData] = None,
        code: str = None,
        success: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListPersonTraceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListPersonTraceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPersonTraceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListPersonTraceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPersonTraceDetailsRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        page_number: int = None,
        page_size: int = None,
        end_time: str = None,
        person_id: str = None,
        start_time: str = None,
        sub_id: str = None,
        data_source_id: str = None,
    ):
        self.corp_id = corp_id
        self.page_number = page_number
        self.page_size = page_size
        self.end_time = end_time
        self.person_id = person_id
        self.start_time = start_time
        self.sub_id = sub_id
        self.data_source_id = data_source_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sub_id is not None:
            result['SubId'] = self.sub_id
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SubId') is not None:
            self.sub_id = m.get('SubId')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        return self


class ListPersonTraceDetailsResponseBodyData(TeaModel):
    def __init__(
        self,
        target_pic_url_path: str = None,
        sub_id: str = None,
        right_bottom_y: str = None,
        left_top_y: str = None,
        pic_url_path: str = None,
        data_source_id: str = None,
        corp_id: str = None,
        shot_time: str = None,
        left_top_x: str = None,
        right_bottom_x: str = None,
        person_id: str = None,
    ):
        self.target_pic_url_path = target_pic_url_path
        self.sub_id = sub_id
        self.right_bottom_y = right_bottom_y
        self.left_top_y = left_top_y
        self.pic_url_path = pic_url_path
        self.data_source_id = data_source_id
        self.corp_id = corp_id
        self.shot_time = shot_time
        self.left_top_x = left_top_x
        self.right_bottom_x = right_bottom_x
        self.person_id = person_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_pic_url_path is not None:
            result['TargetPicUrlPath'] = self.target_pic_url_path
        if self.sub_id is not None:
            result['SubId'] = self.sub_id
        if self.right_bottom_y is not None:
            result['RightBottomY'] = self.right_bottom_y
        if self.left_top_y is not None:
            result['LeftTopY'] = self.left_top_y
        if self.pic_url_path is not None:
            result['PicUrlPath'] = self.pic_url_path
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.shot_time is not None:
            result['ShotTime'] = self.shot_time
        if self.left_top_x is not None:
            result['LeftTopX'] = self.left_top_x
        if self.right_bottom_x is not None:
            result['RightBottomX'] = self.right_bottom_x
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetPicUrlPath') is not None:
            self.target_pic_url_path = m.get('TargetPicUrlPath')
        if m.get('SubId') is not None:
            self.sub_id = m.get('SubId')
        if m.get('RightBottomY') is not None:
            self.right_bottom_y = m.get('RightBottomY')
        if m.get('LeftTopY') is not None:
            self.left_top_y = m.get('LeftTopY')
        if m.get('PicUrlPath') is not None:
            self.pic_url_path = m.get('PicUrlPath')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('ShotTime') is not None:
            self.shot_time = m.get('ShotTime')
        if m.get('LeftTopX') is not None:
            self.left_top_x = m.get('LeftTopX')
        if m.get('RightBottomX') is not None:
            self.right_bottom_x = m.get('RightBottomX')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        return self


class ListPersonTraceDetailsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        data: List[ListPersonTraceDetailsResponseBodyData] = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListPersonTraceDetailsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListPersonTraceDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPersonTraceDetailsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListPersonTraceDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPersonVisitCountRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: str = None,
        end_time: str = None,
        aggregate_type: str = None,
        tag_code: str = None,
        time_aggregate_type: str = None,
        min_val: int = None,
        max_val: int = None,
        count_type: str = None,
    ):
        self.corp_id = corp_id
        self.page_number = page_number
        self.page_size = page_size
        self.start_time = start_time
        self.end_time = end_time
        self.aggregate_type = aggregate_type
        self.tag_code = tag_code
        self.time_aggregate_type = time_aggregate_type
        self.min_val = min_val
        self.max_val = max_val
        self.count_type = count_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.aggregate_type is not None:
            result['AggregateType'] = self.aggregate_type
        if self.tag_code is not None:
            result['TagCode'] = self.tag_code
        if self.time_aggregate_type is not None:
            result['TimeAggregateType'] = self.time_aggregate_type
        if self.min_val is not None:
            result['MinVal'] = self.min_val
        if self.max_val is not None:
            result['MaxVal'] = self.max_val
        if self.count_type is not None:
            result['CountType'] = self.count_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('AggregateType') is not None:
            self.aggregate_type = m.get('AggregateType')
        if m.get('TagCode') is not None:
            self.tag_code = m.get('TagCode')
        if m.get('TimeAggregateType') is not None:
            self.time_aggregate_type = m.get('TimeAggregateType')
        if m.get('MinVal') is not None:
            self.min_val = m.get('MinVal')
        if m.get('MaxVal') is not None:
            self.max_val = m.get('MaxVal')
        if m.get('CountType') is not None:
            self.count_type = m.get('CountType')
        return self


class ListPersonVisitCountResponseBodyData(TeaModel):
    def __init__(
        self,
        day_id: str = None,
        group_id: str = None,
        device_id: str = None,
        tag_code: str = None,
        corp_id: str = None,
        tag_metrics: str = None,
        hour_id: str = None,
        person_id: str = None,
    ):
        self.day_id = day_id
        self.group_id = group_id
        self.device_id = device_id
        self.tag_code = tag_code
        self.corp_id = corp_id
        self.tag_metrics = tag_metrics
        self.hour_id = hour_id
        self.person_id = person_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_id is not None:
            result['DayId'] = self.day_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.tag_code is not None:
            result['TagCode'] = self.tag_code
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.tag_metrics is not None:
            result['TagMetrics'] = self.tag_metrics
        if self.hour_id is not None:
            result['HourId'] = self.hour_id
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DayId') is not None:
            self.day_id = m.get('DayId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('TagCode') is not None:
            self.tag_code = m.get('TagCode')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TagMetrics') is not None:
            self.tag_metrics = m.get('TagMetrics')
        if m.get('HourId') is not None:
            self.hour_id = m.get('HourId')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        return self


class ListPersonVisitCountResponseBody(TeaModel):
    def __init__(
        self,
        total_count: str = None,
        request_id: str = None,
        message: str = None,
        page_size: str = None,
        page_no: str = None,
        data: List[ListPersonVisitCountResponseBodyData] = None,
        code: str = None,
        success: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_no = page_no
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListPersonVisitCountResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListPersonVisitCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPersonVisitCountResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListPersonVisitCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubscribeDeviceRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
    ):
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListSubscribeDeviceResponseBodyDataSubscribeList(TeaModel):
    def __init__(
        self,
        push_config: str = None,
        update_time: str = None,
        device_id: str = None,
        create_time: str = None,
        user_id: str = None,
    ):
        self.push_config = push_config
        self.update_time = update_time
        self.device_id = device_id
        self.create_time = create_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.push_config is not None:
            result['PushConfig'] = self.push_config
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PushConfig') is not None:
            self.push_config = m.get('PushConfig')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListSubscribeDeviceResponseBodyData(TeaModel):
    def __init__(
        self,
        subscribe_list: List[ListSubscribeDeviceResponseBodyDataSubscribeList] = None,
        total_count: int = None,
    ):
        self.subscribe_list = subscribe_list
        self.total_count = total_count

    def validate(self):
        if self.subscribe_list:
            for k in self.subscribe_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SubscribeList'] = []
        if self.subscribe_list is not None:
            for k in self.subscribe_list:
                result['SubscribeList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.subscribe_list = []
        if m.get('SubscribeList') is not None:
            for k in m.get('SubscribeList'):
                temp_model = ListSubscribeDeviceResponseBodyDataSubscribeList()
                self.subscribe_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSubscribeDeviceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListSubscribeDeviceResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListSubscribeDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListSubscribeDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSubscribeDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSubscribeDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTrainLabelRequest(TeaModel):
    def __init__(
        self,
        algorithm_id: str = None,
    ):
        self.algorithm_id = algorithm_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        return self


class ListTrainLabelResponseBodyDataList(TeaModel):
    def __init__(
        self,
        id: str = None,
        label_name: str = None,
        algorithm_id: str = None,
        train_marker_cnt: int = None,
        test_marker_cnt: int = None,
        deleted: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
    ):
        self.id = id
        self.label_name = label_name
        self.algorithm_id = algorithm_id
        self.train_marker_cnt = train_marker_cnt
        self.test_marker_cnt = test_marker_cnt
        self.deleted = deleted
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.label_name is not None:
            result['LabelName'] = self.label_name
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.train_marker_cnt is not None:
            result['TrainMarkerCnt'] = self.train_marker_cnt
        if self.test_marker_cnt is not None:
            result['TestMarkerCnt'] = self.test_marker_cnt
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LabelName') is not None:
            self.label_name = m.get('LabelName')
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('TrainMarkerCnt') is not None:
            self.train_marker_cnt = m.get('TrainMarkerCnt')
        if m.get('TestMarkerCnt') is not None:
            self.test_marker_cnt = m.get('TestMarkerCnt')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        return self


class ListTrainLabelResponseBodyData(TeaModel):
    def __init__(
        self,
        total: int = None,
        list: List[ListTrainLabelResponseBodyDataList] = None,
    ):
        self.total = total
        self.list = list

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total is not None:
            result['Total'] = self.total
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListTrainLabelResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        return self


class ListTrainLabelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        data: ListTrainLabelResponseBodyData = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = ListTrainLabelResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListTrainLabelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTrainLabelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTrainLabelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserGroupsRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        isv_sub_id: str = None,
    ):
        self.corp_id = corp_id
        self.isv_sub_id = isv_sub_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        return self


class ListUserGroupsResponseBodyData(TeaModel):
    def __init__(
        self,
        update_time: str = None,
        isv_sub_id: str = None,
        user_group_id: int = None,
        create_time: str = None,
        user_group_name: str = None,
        user_count: int = None,
        parent_user_group_id: int = None,
        creator: str = None,
    ):
        self.update_time = update_time
        self.isv_sub_id = isv_sub_id
        self.user_group_id = user_group_id
        self.create_time = create_time
        self.user_group_name = user_group_name
        self.user_count = user_count
        self.parent_user_group_id = parent_user_group_id
        self.creator = creator

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        if self.user_count is not None:
            result['UserCount'] = self.user_count
        if self.parent_user_group_id is not None:
            result['ParentUserGroupId'] = self.parent_user_group_id
        if self.creator is not None:
            result['Creator'] = self.creator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')
        if m.get('ParentUserGroupId') is not None:
            self.parent_user_group_id = m.get('ParentUserGroupId')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        return self


class ListUserGroupsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[ListUserGroupsResponseBodyData] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListUserGroupsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListUserGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUserGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUserGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        isv_sub_id: str = None,
        user_name: str = None,
        user_group_id: int = None,
        id_number: str = None,
        face_image_url: str = None,
        address: str = None,
        age: int = None,
        gender: int = None,
        plate_no: str = None,
        phone_no: str = None,
        attachment: str = None,
        biz_id: str = None,
        page_number: int = None,
        page_size: int = None,
        person_list: Dict[str, Any] = None,
        user_list: Dict[str, Any] = None,
        matching_rate_threshold: str = None,
    ):
        self.corp_id = corp_id
        self.isv_sub_id = isv_sub_id
        self.user_name = user_name
        self.user_group_id = user_group_id
        self.id_number = id_number
        self.face_image_url = face_image_url
        self.address = address
        self.age = age
        self.gender = gender
        self.plate_no = plate_no
        self.phone_no = phone_no
        self.attachment = attachment
        self.biz_id = biz_id
        self.page_number = page_number
        self.page_size = page_size
        self.person_list = person_list
        self.user_list = user_list
        self.matching_rate_threshold = matching_rate_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.id_number is not None:
            result['IdNumber'] = self.id_number
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.address is not None:
            result['Address'] = self.address
        if self.age is not None:
            result['Age'] = self.age
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.plate_no is not None:
            result['PlateNo'] = self.plate_no
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        if self.attachment is not None:
            result['Attachment'] = self.attachment
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.person_list is not None:
            result['PersonList'] = self.person_list
        if self.user_list is not None:
            result['UserList'] = self.user_list
        if self.matching_rate_threshold is not None:
            result['MatchingRateThreshold'] = self.matching_rate_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('IdNumber') is not None:
            self.id_number = m.get('IdNumber')
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('PlateNo') is not None:
            self.plate_no = m.get('PlateNo')
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        if m.get('Attachment') is not None:
            self.attachment = m.get('Attachment')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PersonList') is not None:
            self.person_list = m.get('PersonList')
        if m.get('UserList') is not None:
            self.user_list = m.get('UserList')
        if m.get('MatchingRateThreshold') is not None:
            self.matching_rate_threshold = m.get('MatchingRateThreshold')
        return self


class ListUsersShrinkRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        isv_sub_id: str = None,
        user_name: str = None,
        user_group_id: int = None,
        id_number: str = None,
        face_image_url: str = None,
        address: str = None,
        age: int = None,
        gender: int = None,
        plate_no: str = None,
        phone_no: str = None,
        attachment: str = None,
        biz_id: str = None,
        page_number: int = None,
        page_size: int = None,
        person_list_shrink: str = None,
        user_list_shrink: str = None,
        matching_rate_threshold: str = None,
    ):
        self.corp_id = corp_id
        self.isv_sub_id = isv_sub_id
        self.user_name = user_name
        self.user_group_id = user_group_id
        self.id_number = id_number
        self.face_image_url = face_image_url
        self.address = address
        self.age = age
        self.gender = gender
        self.plate_no = plate_no
        self.phone_no = phone_no
        self.attachment = attachment
        self.biz_id = biz_id
        self.page_number = page_number
        self.page_size = page_size
        self.person_list_shrink = person_list_shrink
        self.user_list_shrink = user_list_shrink
        self.matching_rate_threshold = matching_rate_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.id_number is not None:
            result['IdNumber'] = self.id_number
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.address is not None:
            result['Address'] = self.address
        if self.age is not None:
            result['Age'] = self.age
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.plate_no is not None:
            result['PlateNo'] = self.plate_no
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        if self.attachment is not None:
            result['Attachment'] = self.attachment
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.person_list_shrink is not None:
            result['PersonList'] = self.person_list_shrink
        if self.user_list_shrink is not None:
            result['UserList'] = self.user_list_shrink
        if self.matching_rate_threshold is not None:
            result['MatchingRateThreshold'] = self.matching_rate_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('IdNumber') is not None:
            self.id_number = m.get('IdNumber')
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('PlateNo') is not None:
            self.plate_no = m.get('PlateNo')
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        if m.get('Attachment') is not None:
            self.attachment = m.get('Attachment')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PersonList') is not None:
            self.person_list_shrink = m.get('PersonList')
        if m.get('UserList') is not None:
            self.user_list_shrink = m.get('UserList')
        if m.get('MatchingRateThreshold') is not None:
            self.matching_rate_threshold = m.get('MatchingRateThreshold')
        return self


class ListUsersResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        isv_sub_id: str = None,
        gender: str = None,
        face_image_url: str = None,
        user_group_id: int = None,
        user_id: int = None,
        matching_rate: str = None,
        biz_id: str = None,
        attachment: str = None,
        age: str = None,
        id_number: str = None,
        person_id: str = None,
        user_name: str = None,
    ):
        self.isv_sub_id = isv_sub_id
        self.gender = gender
        self.face_image_url = face_image_url
        self.user_group_id = user_group_id
        self.user_id = user_id
        self.matching_rate = matching_rate
        self.biz_id = biz_id
        self.attachment = attachment
        self.age = age
        self.id_number = id_number
        self.person_id = person_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.matching_rate is not None:
            result['MatchingRate'] = self.matching_rate
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.attachment is not None:
            result['Attachment'] = self.attachment
        if self.age is not None:
            result['Age'] = self.age
        if self.id_number is not None:
            result['IdNumber'] = self.id_number
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('MatchingRate') is not None:
            self.matching_rate = m.get('MatchingRate')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Attachment') is not None:
            self.attachment = m.get('Attachment')
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('IdNumber') is not None:
            self.id_number = m.get('IdNumber')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListUsersResponseBodyData(TeaModel):
    def __init__(
        self,
        success: int = None,
        records: List[ListUsersResponseBodyDataRecords] = None,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.success = success
        self.records = records
        self.page_number = page_number
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListUsersResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListUsersResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListUsersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUsersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RaiseDevicesStorageRequest(TeaModel):
    def __init__(
        self,
        json: str = None,
    ):
        self.json = json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json is not None:
            result['Json'] = self.json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Json') is not None:
            self.json = m.get('Json')
        return self


class RaiseDevicesStorageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: bool = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class RaiseDevicesStorageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RaiseDevicesStorageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RaiseDevicesStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeFaceQualityRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        pic_content: str = None,
        pic_format: str = None,
        pic_url: str = None,
    ):
        self.corp_id = corp_id
        self.pic_content = pic_content
        self.pic_format = pic_format
        self.pic_url = pic_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.pic_content is not None:
            result['PicContent'] = self.pic_content
        if self.pic_format is not None:
            result['PicFormat'] = self.pic_format
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('PicContent') is not None:
            self.pic_content = m.get('PicContent')
        if m.get('PicFormat') is not None:
            self.pic_format = m.get('PicFormat')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        return self


class RecognizeFaceQualityResponseBodyDataAttributes(TeaModel):
    def __init__(
        self,
        face_score: str = None,
        right_bottom_y: int = None,
        left_top_y: int = None,
        face_style: str = None,
        face_quality: str = None,
        left_top_x: int = None,
        right_bottom_x: int = None,
        target_image_storage_path: str = None,
    ):
        self.face_score = face_score
        self.right_bottom_y = right_bottom_y
        self.left_top_y = left_top_y
        self.face_style = face_style
        self.face_quality = face_quality
        self.left_top_x = left_top_x
        self.right_bottom_x = right_bottom_x
        self.target_image_storage_path = target_image_storage_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_score is not None:
            result['FaceScore'] = self.face_score
        if self.right_bottom_y is not None:
            result['RightBottomY'] = self.right_bottom_y
        if self.left_top_y is not None:
            result['LeftTopY'] = self.left_top_y
        if self.face_style is not None:
            result['FaceStyle'] = self.face_style
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        if self.left_top_x is not None:
            result['LeftTopX'] = self.left_top_x
        if self.right_bottom_x is not None:
            result['RightBottomX'] = self.right_bottom_x
        if self.target_image_storage_path is not None:
            result['TargetImageStoragePath'] = self.target_image_storage_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceScore') is not None:
            self.face_score = m.get('FaceScore')
        if m.get('RightBottomY') is not None:
            self.right_bottom_y = m.get('RightBottomY')
        if m.get('LeftTopY') is not None:
            self.left_top_y = m.get('LeftTopY')
        if m.get('FaceStyle') is not None:
            self.face_style = m.get('FaceStyle')
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        if m.get('LeftTopX') is not None:
            self.left_top_x = m.get('LeftTopX')
        if m.get('RightBottomX') is not None:
            self.right_bottom_x = m.get('RightBottomX')
        if m.get('TargetImageStoragePath') is not None:
            self.target_image_storage_path = m.get('TargetImageStoragePath')
        return self


class RecognizeFaceQualityResponseBodyData(TeaModel):
    def __init__(
        self,
        quality_score: str = None,
        description: str = None,
        attributes: RecognizeFaceQualityResponseBodyDataAttributes = None,
    ):
        self.quality_score = quality_score
        self.description = description
        self.attributes = attributes

    def validate(self):
        if self.attributes:
            self.attributes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quality_score is not None:
            result['QualityScore'] = self.quality_score
        if self.description is not None:
            result['Description'] = self.description
        if self.attributes is not None:
            result['Attributes'] = self.attributes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QualityScore') is not None:
            self.quality_score = m.get('QualityScore')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Attributes') is not None:
            temp_model = RecognizeFaceQualityResponseBodyDataAttributes()
            self.attributes = temp_model.from_map(m['Attributes'])
        return self


class RecognizeFaceQualityResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: RecognizeFaceQualityResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizeFaceQualityResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class RecognizeFaceQualityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeFaceQualityResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RecognizeFaceQualityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecognizeImageRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        pic_content: str = None,
        pic_format: str = None,
        pic_url: str = None,
    ):
        self.corp_id = corp_id
        self.pic_content = pic_content
        self.pic_format = pic_format
        self.pic_url = pic_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.pic_content is not None:
            result['PicContent'] = self.pic_content
        if self.pic_format is not None:
            result['PicFormat'] = self.pic_format
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('PicContent') is not None:
            self.pic_content = m.get('PicContent')
        if m.get('PicFormat') is not None:
            self.pic_format = m.get('PicFormat')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        return self


class RecognizeImageResponseBodyDataBodyList(TeaModel):
    def __init__(
        self,
        respirator_color: str = None,
        right_bottom_y: str = None,
        feature: str = None,
        left_top_y: str = None,
        image_base_six_four: str = None,
        file_name: str = None,
        right_bottom_x: str = None,
        local_feature: str = None,
        left_top_x: str = None,
    ):
        self.respirator_color = respirator_color
        self.right_bottom_y = right_bottom_y
        self.feature = feature
        self.left_top_y = left_top_y
        self.image_base_six_four = image_base_six_four
        self.file_name = file_name
        self.right_bottom_x = right_bottom_x
        self.local_feature = local_feature
        self.left_top_x = left_top_x

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.respirator_color is not None:
            result['RespiratorColor'] = self.respirator_color
        if self.right_bottom_y is not None:
            result['RightBottomY'] = self.right_bottom_y
        if self.feature is not None:
            result['Feature'] = self.feature
        if self.left_top_y is not None:
            result['LeftTopY'] = self.left_top_y
        if self.image_base_six_four is not None:
            result['ImageBaseSixFour'] = self.image_base_six_four
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.right_bottom_x is not None:
            result['RightBottomX'] = self.right_bottom_x
        if self.local_feature is not None:
            result['LocalFeature'] = self.local_feature
        if self.left_top_x is not None:
            result['LeftTopX'] = self.left_top_x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RespiratorColor') is not None:
            self.respirator_color = m.get('RespiratorColor')
        if m.get('RightBottomY') is not None:
            self.right_bottom_y = m.get('RightBottomY')
        if m.get('Feature') is not None:
            self.feature = m.get('Feature')
        if m.get('LeftTopY') is not None:
            self.left_top_y = m.get('LeftTopY')
        if m.get('ImageBaseSixFour') is not None:
            self.image_base_six_four = m.get('ImageBaseSixFour')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('RightBottomX') is not None:
            self.right_bottom_x = m.get('RightBottomX')
        if m.get('LocalFeature') is not None:
            self.local_feature = m.get('LocalFeature')
        if m.get('LeftTopX') is not None:
            self.left_top_x = m.get('LeftTopX')
        return self


class RecognizeImageResponseBodyDataFaceList(TeaModel):
    def __init__(
        self,
        quality: float = None,
        respirator_color: str = None,
        key_point_quality: float = None,
        right_bottom_y: str = None,
        feature: str = None,
        left_top_y: str = None,
        image_base_six_four: str = None,
        file_name: str = None,
        right_bottom_x: str = None,
        local_feature: str = None,
        left_top_x: str = None,
    ):
        self.quality = quality
        self.respirator_color = respirator_color
        self.key_point_quality = key_point_quality
        self.right_bottom_y = right_bottom_y
        self.feature = feature
        self.left_top_y = left_top_y
        self.image_base_six_four = image_base_six_four
        self.file_name = file_name
        self.right_bottom_x = right_bottom_x
        self.local_feature = local_feature
        self.left_top_x = left_top_x

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quality is not None:
            result['Quality'] = self.quality
        if self.respirator_color is not None:
            result['RespiratorColor'] = self.respirator_color
        if self.key_point_quality is not None:
            result['KeyPointQuality'] = self.key_point_quality
        if self.right_bottom_y is not None:
            result['RightBottomY'] = self.right_bottom_y
        if self.feature is not None:
            result['Feature'] = self.feature
        if self.left_top_y is not None:
            result['LeftTopY'] = self.left_top_y
        if self.image_base_six_four is not None:
            result['ImageBaseSixFour'] = self.image_base_six_four
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.right_bottom_x is not None:
            result['RightBottomX'] = self.right_bottom_x
        if self.local_feature is not None:
            result['LocalFeature'] = self.local_feature
        if self.left_top_x is not None:
            result['LeftTopX'] = self.left_top_x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')
        if m.get('RespiratorColor') is not None:
            self.respirator_color = m.get('RespiratorColor')
        if m.get('KeyPointQuality') is not None:
            self.key_point_quality = m.get('KeyPointQuality')
        if m.get('RightBottomY') is not None:
            self.right_bottom_y = m.get('RightBottomY')
        if m.get('Feature') is not None:
            self.feature = m.get('Feature')
        if m.get('LeftTopY') is not None:
            self.left_top_y = m.get('LeftTopY')
        if m.get('ImageBaseSixFour') is not None:
            self.image_base_six_four = m.get('ImageBaseSixFour')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('RightBottomX') is not None:
            self.right_bottom_x = m.get('RightBottomX')
        if m.get('LocalFeature') is not None:
            self.local_feature = m.get('LocalFeature')
        if m.get('LeftTopX') is not None:
            self.left_top_x = m.get('LeftTopX')
        return self


class RecognizeImageResponseBodyData(TeaModel):
    def __init__(
        self,
        body_list: List[RecognizeImageResponseBodyDataBodyList] = None,
        face_list: List[RecognizeImageResponseBodyDataFaceList] = None,
    ):
        self.body_list = body_list
        self.face_list = face_list

    def validate(self):
        if self.body_list:
            for k in self.body_list:
                if k:
                    k.validate()
        if self.face_list:
            for k in self.face_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BodyList'] = []
        if self.body_list is not None:
            for k in self.body_list:
                result['BodyList'].append(k.to_map() if k else None)
        result['FaceList'] = []
        if self.face_list is not None:
            for k in self.face_list:
                result['FaceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body_list = []
        if m.get('BodyList') is not None:
            for k in m.get('BodyList'):
                temp_model = RecognizeImageResponseBodyDataBodyList()
                self.body_list.append(temp_model.from_map(k))
        self.face_list = []
        if m.get('FaceList') is not None:
            for k in m.get('FaceList'):
                temp_model = RecognizeImageResponseBodyDataFaceList()
                self.face_list.append(temp_model.from_map(k))
        return self


class RecognizeImageResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: RecognizeImageResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = RecognizeImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class RecognizeImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecognizeImageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RecognizeImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterDeviceRequest(TeaModel):
    def __init__(
        self,
        device_sn: str = None,
        device_id: str = None,
        server_id: str = None,
        device_time_stamp: str = None,
    ):
        self.device_sn = device_sn
        self.device_id = device_id
        self.server_id = server_id
        self.device_time_stamp = device_time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.device_time_stamp is not None:
            result['DeviceTimeStamp'] = self.device_time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('DeviceTimeStamp') is not None:
            self.device_time_stamp = m.get('DeviceTimeStamp')
        return self


class RegisterDeviceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        retry_interval: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.retry_interval = retry_interval
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.retry_interval is not None:
            result['RetryInterval'] = self.retry_interval
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RetryInterval') is not None:
            self.retry_interval = m.get('RetryInterval')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class RegisterDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RegisterDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RegisterDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportDeviceCapacityRequestStreamCapacities(TeaModel):
    def __init__(
        self,
        encode_format: str = None,
        gov_length_range: str = None,
        max_frame_rate: str = None,
        bitrate_range: str = None,
        max_stream: str = None,
        resolution: str = None,
    ):
        self.encode_format = encode_format
        self.gov_length_range = gov_length_range
        self.max_frame_rate = max_frame_rate
        self.bitrate_range = bitrate_range
        self.max_stream = max_stream
        self.resolution = resolution

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_format is not None:
            result['EncodeFormat'] = self.encode_format
        if self.gov_length_range is not None:
            result['GovLengthRange'] = self.gov_length_range
        if self.max_frame_rate is not None:
            result['MaxFrameRate'] = self.max_frame_rate
        if self.bitrate_range is not None:
            result['BitrateRange'] = self.bitrate_range
        if self.max_stream is not None:
            result['MaxStream'] = self.max_stream
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeFormat') is not None:
            self.encode_format = m.get('EncodeFormat')
        if m.get('GovLengthRange') is not None:
            self.gov_length_range = m.get('GovLengthRange')
        if m.get('MaxFrameRate') is not None:
            self.max_frame_rate = m.get('MaxFrameRate')
        if m.get('BitrateRange') is not None:
            self.bitrate_range = m.get('BitrateRange')
        if m.get('MaxStream') is not None:
            self.max_stream = m.get('MaxStream')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        return self


class ReportDeviceCapacityRequest(TeaModel):
    def __init__(
        self,
        longitude: str = None,
        latitude: str = None,
        audio_format: str = None,
        preset_num: str = None,
        ptzcapacity: str = None,
        device_sn: str = None,
        device_time_stamp: str = None,
        stream_capacities: List[ReportDeviceCapacityRequestStreamCapacities] = None,
    ):
        self.longitude = longitude
        self.latitude = latitude
        self.audio_format = audio_format
        self.preset_num = preset_num
        self.ptzcapacity = ptzcapacity
        self.device_sn = device_sn
        self.device_time_stamp = device_time_stamp
        self.stream_capacities = stream_capacities

    def validate(self):
        if self.stream_capacities:
            for k in self.stream_capacities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.audio_format is not None:
            result['AudioFormat'] = self.audio_format
        if self.preset_num is not None:
            result['PresetNum'] = self.preset_num
        if self.ptzcapacity is not None:
            result['PTZCapacity'] = self.ptzcapacity
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.device_time_stamp is not None:
            result['DeviceTimeStamp'] = self.device_time_stamp
        result['StreamCapacities'] = []
        if self.stream_capacities is not None:
            for k in self.stream_capacities:
                result['StreamCapacities'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('AudioFormat') is not None:
            self.audio_format = m.get('AudioFormat')
        if m.get('PresetNum') is not None:
            self.preset_num = m.get('PresetNum')
        if m.get('PTZCapacity') is not None:
            self.ptzcapacity = m.get('PTZCapacity')
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('DeviceTimeStamp') is not None:
            self.device_time_stamp = m.get('DeviceTimeStamp')
        self.stream_capacities = []
        if m.get('StreamCapacities') is not None:
            for k in m.get('StreamCapacities'):
                temp_model = ReportDeviceCapacityRequestStreamCapacities()
                self.stream_capacities.append(temp_model.from_map(k))
        return self


class ReportDeviceCapacityResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        retry_interval: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.retry_interval = retry_interval
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.retry_interval is not None:
            result['RetryInterval'] = self.retry_interval
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RetryInterval') is not None:
            self.retry_interval = m.get('RetryInterval')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ReportDeviceCapacityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReportDeviceCapacityResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReportDeviceCapacityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RetryStartDeployRequest(TeaModel):
    def __init__(
        self,
        algorithm_id: str = None,
    ):
        self.algorithm_id = algorithm_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        return self


class RetryStartDeployResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.message = message
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class RetryStartDeployResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RetryStartDeployResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RetryStartDeployResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SampleListRequest(TeaModel):
    def __init__(
        self,
        algorithm_id: str = None,
        label_id: str = None,
        is_marker: str = None,
        type: str = None,
        usages: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.algorithm_id = algorithm_id
        self.label_id = label_id
        self.is_marker = is_marker
        self.type = type
        self.usages = usages
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        if self.is_marker is not None:
            result['IsMarker'] = self.is_marker
        if self.type is not None:
            result['Type'] = self.type
        if self.usages is not None:
            result['Usages'] = self.usages
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        if m.get('IsMarker') is not None:
            self.is_marker = m.get('IsMarker')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Usages') is not None:
            self.usages = m.get('Usages')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class SampleListResponseBodyDataList(TeaModel):
    def __init__(
        self,
        id: str = None,
        algorithm_id: str = None,
        user_id: str = None,
        type: str = None,
        usages: str = None,
        content: str = None,
        url: str = None,
        marker_count: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
    ):
        self.id = id
        self.algorithm_id = algorithm_id
        self.user_id = user_id
        self.type = type
        self.usages = usages
        self.content = content
        self.url = url
        self.marker_count = marker_count
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.type is not None:
            result['Type'] = self.type
        if self.usages is not None:
            result['Usages'] = self.usages
        if self.content is not None:
            result['Content'] = self.content
        if self.url is not None:
            result['Url'] = self.url
        if self.marker_count is not None:
            result['MarkerCount'] = self.marker_count
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Usages') is not None:
            self.usages = m.get('Usages')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('MarkerCount') is not None:
            self.marker_count = m.get('MarkerCount')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        return self


class SampleListResponseBodyData(TeaModel):
    def __init__(
        self,
        total: int = None,
        list: List[SampleListResponseBodyDataList] = None,
    ):
        self.total = total
        self.list = list

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total is not None:
            result['Total'] = self.total
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = SampleListResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        return self


class SampleListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        data: SampleListResponseBodyData = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = SampleListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class SampleListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SampleListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SampleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveVideoSummaryTaskVideoRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        task_id: int = None,
        save_video: bool = None,
    ):
        self.corp_id = corp_id
        self.task_id = task_id
        self.save_video = save_video

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.save_video is not None:
            result['SaveVideo'] = self.save_video
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('SaveVideo') is not None:
            self.save_video = m.get('SaveVideo')
        return self


class SaveVideoSummaryTaskVideoResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class SaveVideoSummaryTaskVideoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveVideoSummaryTaskVideoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SaveVideoSummaryTaskVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchBodyRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        gb_id: str = None,
        start_time_stamp: int = None,
        end_time_stamp: int = None,
        page_no: int = None,
        page_size: int = None,
        option_list: Dict[str, Any] = None,
    ):
        self.corp_id = corp_id
        self.gb_id = gb_id
        self.start_time_stamp = start_time_stamp
        self.end_time_stamp = end_time_stamp
        self.page_no = page_no
        self.page_size = page_size
        self.option_list = option_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.start_time_stamp is not None:
            result['StartTimeStamp'] = self.start_time_stamp
        if self.end_time_stamp is not None:
            result['EndTimeStamp'] = self.end_time_stamp
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.option_list is not None:
            result['OptionList'] = self.option_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('StartTimeStamp') is not None:
            self.start_time_stamp = m.get('StartTimeStamp')
        if m.get('EndTimeStamp') is not None:
            self.end_time_stamp = m.get('EndTimeStamp')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('OptionList') is not None:
            self.option_list = m.get('OptionList')
        return self


class SearchBodyShrinkRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        gb_id: str = None,
        start_time_stamp: int = None,
        end_time_stamp: int = None,
        page_no: int = None,
        page_size: int = None,
        option_list_shrink: str = None,
    ):
        self.corp_id = corp_id
        self.gb_id = gb_id
        self.start_time_stamp = start_time_stamp
        self.end_time_stamp = end_time_stamp
        self.page_no = page_no
        self.page_size = page_size
        self.option_list_shrink = option_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.start_time_stamp is not None:
            result['StartTimeStamp'] = self.start_time_stamp
        if self.end_time_stamp is not None:
            result['EndTimeStamp'] = self.end_time_stamp
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.option_list_shrink is not None:
            result['OptionList'] = self.option_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('StartTimeStamp') is not None:
            self.start_time_stamp = m.get('StartTimeStamp')
        if m.get('EndTimeStamp') is not None:
            self.end_time_stamp = m.get('EndTimeStamp')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('OptionList') is not None:
            self.option_list_shrink = m.get('OptionList')
        return self


class SearchBodyResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        gb_id: str = None,
        target_image_url: str = None,
        right_bottom_y: float = None,
        image_url: str = None,
        left_top_y: float = None,
        score: float = None,
        left_top_x: float = None,
        right_bottom_x: float = None,
    ):
        self.gb_id = gb_id
        self.target_image_url = target_image_url
        self.right_bottom_y = right_bottom_y
        self.image_url = image_url
        self.left_top_y = left_top_y
        self.score = score
        self.left_top_x = left_top_x
        self.right_bottom_x = right_bottom_x

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.target_image_url is not None:
            result['TargetImageUrl'] = self.target_image_url
        if self.right_bottom_y is not None:
            result['RightBottomY'] = self.right_bottom_y
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.left_top_y is not None:
            result['LeftTopY'] = self.left_top_y
        if self.score is not None:
            result['Score'] = self.score
        if self.left_top_x is not None:
            result['LeftTopX'] = self.left_top_x
        if self.right_bottom_x is not None:
            result['RightBottomX'] = self.right_bottom_x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('TargetImageUrl') is not None:
            self.target_image_url = m.get('TargetImageUrl')
        if m.get('RightBottomY') is not None:
            self.right_bottom_y = m.get('RightBottomY')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('LeftTopY') is not None:
            self.left_top_y = m.get('LeftTopY')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('LeftTopX') is not None:
            self.left_top_x = m.get('LeftTopX')
        if m.get('RightBottomX') is not None:
            self.right_bottom_x = m.get('RightBottomX')
        return self


class SearchBodyResponseBodyData(TeaModel):
    def __init__(
        self,
        records: List[SearchBodyResponseBodyDataRecords] = None,
        page_no: int = None,
        total_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.records = records
        self.page_no = page_no
        self.total_page = total_page
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = SearchBodyResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchBodyResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: SearchBodyResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = SearchBodyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class SearchBodyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchBodyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SearchBodyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchFaceRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        gb_id: str = None,
        start_time_stamp: int = None,
        end_time_stamp: int = None,
        page_no: int = None,
        page_size: int = None,
        option_list: Dict[str, Any] = None,
    ):
        self.corp_id = corp_id
        self.gb_id = gb_id
        self.start_time_stamp = start_time_stamp
        self.end_time_stamp = end_time_stamp
        self.page_no = page_no
        self.page_size = page_size
        self.option_list = option_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.start_time_stamp is not None:
            result['StartTimeStamp'] = self.start_time_stamp
        if self.end_time_stamp is not None:
            result['EndTimeStamp'] = self.end_time_stamp
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.option_list is not None:
            result['OptionList'] = self.option_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('StartTimeStamp') is not None:
            self.start_time_stamp = m.get('StartTimeStamp')
        if m.get('EndTimeStamp') is not None:
            self.end_time_stamp = m.get('EndTimeStamp')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('OptionList') is not None:
            self.option_list = m.get('OptionList')
        return self


class SearchFaceShrinkRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        gb_id: str = None,
        start_time_stamp: int = None,
        end_time_stamp: int = None,
        page_no: int = None,
        page_size: int = None,
        option_list_shrink: str = None,
    ):
        self.corp_id = corp_id
        self.gb_id = gb_id
        self.start_time_stamp = start_time_stamp
        self.end_time_stamp = end_time_stamp
        self.page_no = page_no
        self.page_size = page_size
        self.option_list_shrink = option_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.start_time_stamp is not None:
            result['StartTimeStamp'] = self.start_time_stamp
        if self.end_time_stamp is not None:
            result['EndTimeStamp'] = self.end_time_stamp
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.option_list_shrink is not None:
            result['OptionList'] = self.option_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('StartTimeStamp') is not None:
            self.start_time_stamp = m.get('StartTimeStamp')
        if m.get('EndTimeStamp') is not None:
            self.end_time_stamp = m.get('EndTimeStamp')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('OptionList') is not None:
            self.option_list_shrink = m.get('OptionList')
        return self


class SearchFaceResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        gb_id: str = None,
        target_image_url: str = None,
        right_bottom_y: float = None,
        image_url: str = None,
        left_top_y: float = None,
        score: float = None,
        source_id: str = None,
        right_bottom_x: float = None,
        left_top_x: float = None,
        match_suggestion: str = None,
    ):
        self.gb_id = gb_id
        self.target_image_url = target_image_url
        self.right_bottom_y = right_bottom_y
        self.image_url = image_url
        self.left_top_y = left_top_y
        self.score = score
        self.source_id = source_id
        self.right_bottom_x = right_bottom_x
        self.left_top_x = left_top_x
        self.match_suggestion = match_suggestion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.target_image_url is not None:
            result['TargetImageUrl'] = self.target_image_url
        if self.right_bottom_y is not None:
            result['RightBottomY'] = self.right_bottom_y
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.left_top_y is not None:
            result['LeftTopY'] = self.left_top_y
        if self.score is not None:
            result['Score'] = self.score
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.right_bottom_x is not None:
            result['RightBottomX'] = self.right_bottom_x
        if self.left_top_x is not None:
            result['LeftTopX'] = self.left_top_x
        if self.match_suggestion is not None:
            result['MatchSuggestion'] = self.match_suggestion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('TargetImageUrl') is not None:
            self.target_image_url = m.get('TargetImageUrl')
        if m.get('RightBottomY') is not None:
            self.right_bottom_y = m.get('RightBottomY')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('LeftTopY') is not None:
            self.left_top_y = m.get('LeftTopY')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('RightBottomX') is not None:
            self.right_bottom_x = m.get('RightBottomX')
        if m.get('LeftTopX') is not None:
            self.left_top_x = m.get('LeftTopX')
        if m.get('MatchSuggestion') is not None:
            self.match_suggestion = m.get('MatchSuggestion')
        return self


class SearchFaceResponseBodyData(TeaModel):
    def __init__(
        self,
        records: List[SearchFaceResponseBodyDataRecords] = None,
        page_no: int = None,
        total_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.records = records
        self.page_no = page_no
        self.total_page = total_page
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = SearchFaceResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchFaceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: SearchFaceResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = SearchFaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class SearchFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchFaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SearchFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchObjectRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        object_type: str = None,
        start_time: int = None,
        end_time: int = None,
        page_number: int = None,
        page_size: int = None,
        device_list: Dict[str, Any] = None,
        pic_url: str = None,
        conditions: Dict[str, Any] = None,
        algorithm_type: str = None,
        image_path: Dict[str, Any] = None,
    ):
        self.corp_id = corp_id
        self.object_type = object_type
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.device_list = device_list
        self.pic_url = pic_url
        self.conditions = conditions
        self.algorithm_type = algorithm_type
        self.image_path = image_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.device_list is not None:
            result['DeviceList'] = self.device_list
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.conditions is not None:
            result['Conditions'] = self.conditions
        if self.algorithm_type is not None:
            result['AlgorithmType'] = self.algorithm_type
        if self.image_path is not None:
            result['ImagePath'] = self.image_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('DeviceList') is not None:
            self.device_list = m.get('DeviceList')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('Conditions') is not None:
            self.conditions = m.get('Conditions')
        if m.get('AlgorithmType') is not None:
            self.algorithm_type = m.get('AlgorithmType')
        if m.get('ImagePath') is not None:
            self.image_path = m.get('ImagePath')
        return self


class SearchObjectShrinkRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        object_type: str = None,
        start_time: int = None,
        end_time: int = None,
        page_number: int = None,
        page_size: int = None,
        device_list_shrink: str = None,
        pic_url: str = None,
        conditions_shrink: str = None,
        algorithm_type: str = None,
        image_path_shrink: str = None,
    ):
        self.corp_id = corp_id
        self.object_type = object_type
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.device_list_shrink = device_list_shrink
        self.pic_url = pic_url
        self.conditions_shrink = conditions_shrink
        self.algorithm_type = algorithm_type
        self.image_path_shrink = image_path_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.device_list_shrink is not None:
            result['DeviceList'] = self.device_list_shrink
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.conditions_shrink is not None:
            result['Conditions'] = self.conditions_shrink
        if self.algorithm_type is not None:
            result['AlgorithmType'] = self.algorithm_type
        if self.image_path_shrink is not None:
            result['ImagePath'] = self.image_path_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('DeviceList') is not None:
            self.device_list_shrink = m.get('DeviceList')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('Conditions') is not None:
            self.conditions_shrink = m.get('Conditions')
        if m.get('AlgorithmType') is not None:
            self.algorithm_type = m.get('AlgorithmType')
        if m.get('ImagePath') is not None:
            self.image_path_shrink = m.get('ImagePath')
        return self


class SearchObjectResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        compare_result: str = None,
        right_btm_x: int = None,
        score: float = None,
        source_image_url: str = None,
        source_id: str = None,
        right_btm_y: int = None,
        target_image_url: str = None,
        left_top_y: int = None,
        target_image_path: str = None,
        shot_time: int = None,
        left_top_x: int = None,
        source_image_path: str = None,
    ):
        self.device_id = device_id
        self.compare_result = compare_result
        self.right_btm_x = right_btm_x
        self.score = score
        self.source_image_url = source_image_url
        self.source_id = source_id
        self.right_btm_y = right_btm_y
        self.target_image_url = target_image_url
        self.left_top_y = left_top_y
        self.target_image_path = target_image_path
        self.shot_time = shot_time
        self.left_top_x = left_top_x
        self.source_image_path = source_image_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceID'] = self.device_id
        if self.compare_result is not None:
            result['CompareResult'] = self.compare_result
        if self.right_btm_x is not None:
            result['RightBtmX'] = self.right_btm_x
        if self.score is not None:
            result['Score'] = self.score
        if self.source_image_url is not None:
            result['SourceImageUrl'] = self.source_image_url
        if self.source_id is not None:
            result['SourceID'] = self.source_id
        if self.right_btm_y is not None:
            result['RightBtmY'] = self.right_btm_y
        if self.target_image_url is not None:
            result['TargetImageUrl'] = self.target_image_url
        if self.left_top_y is not None:
            result['LeftTopY'] = self.left_top_y
        if self.target_image_path is not None:
            result['TargetImagePath'] = self.target_image_path
        if self.shot_time is not None:
            result['ShotTime'] = self.shot_time
        if self.left_top_x is not None:
            result['LeftTopX'] = self.left_top_x
        if self.source_image_path is not None:
            result['SourceImagePath'] = self.source_image_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceID') is not None:
            self.device_id = m.get('DeviceID')
        if m.get('CompareResult') is not None:
            self.compare_result = m.get('CompareResult')
        if m.get('RightBtmX') is not None:
            self.right_btm_x = m.get('RightBtmX')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('SourceImageUrl') is not None:
            self.source_image_url = m.get('SourceImageUrl')
        if m.get('SourceID') is not None:
            self.source_id = m.get('SourceID')
        if m.get('RightBtmY') is not None:
            self.right_btm_y = m.get('RightBtmY')
        if m.get('TargetImageUrl') is not None:
            self.target_image_url = m.get('TargetImageUrl')
        if m.get('LeftTopY') is not None:
            self.left_top_y = m.get('LeftTopY')
        if m.get('TargetImagePath') is not None:
            self.target_image_path = m.get('TargetImagePath')
        if m.get('ShotTime') is not None:
            self.shot_time = m.get('ShotTime')
        if m.get('LeftTopX') is not None:
            self.left_top_x = m.get('LeftTopX')
        if m.get('SourceImagePath') is not None:
            self.source_image_path = m.get('SourceImagePath')
        return self


class SearchObjectResponseBodyData(TeaModel):
    def __init__(
        self,
        records: List[SearchObjectResponseBodyDataRecords] = None,
        total_page: int = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.records = records
        self.total_page = total_page
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = SearchObjectResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchObjectResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: SearchObjectResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = SearchObjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class SearchObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchObjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SearchObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDeployRequest(TeaModel):
    def __init__(
        self,
        algorithm_id: str = None,
    ):
        self.algorithm_id = algorithm_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        return self


class StartDeployResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class StartDeployResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartDeployResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartDeployResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartTrainRequest(TeaModel):
    def __init__(
        self,
        algorithm_id: str = None,
    ):
        self.algorithm_id = algorithm_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        return self


class StartTrainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class StartTrainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartTrainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartTrainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDeployRequest(TeaModel):
    def __init__(
        self,
        algorithm_id: str = None,
    ):
        self.algorithm_id = algorithm_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        return self


class StopDeployResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class StopDeployResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopDeployResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopDeployResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopMonitorRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        algorithm_vendor: str = None,
    ):
        self.task_id = task_id
        self.algorithm_vendor = algorithm_vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.algorithm_vendor is not None:
            result['AlgorithmVendor'] = self.algorithm_vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('AlgorithmVendor') is not None:
            self.algorithm_vendor = m.get('AlgorithmVendor')
        return self


class StopMonitorResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class StopMonitorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopMonitorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopTrainRequest(TeaModel):
    def __init__(
        self,
        algorithm_id: str = None,
    ):
        self.algorithm_id = algorithm_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        return self


class StopTrainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class StopTrainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopTrainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopTrainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubscribeDeviceEventRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        push_config: str = None,
    ):
        self.device_id = device_id
        self.push_config = push_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.push_config is not None:
            result['PushConfig'] = self.push_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('PushConfig') is not None:
            self.push_config = m.get('PushConfig')
        return self


class SubscribeDeviceEventResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class SubscribeDeviceEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubscribeDeviceEventResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SubscribeDeviceEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubscribeSpaceEventRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        push_config: str = None,
    ):
        self.space_id = space_id
        self.push_config = push_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.push_config is not None:
            result['PushConfig'] = self.push_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('PushConfig') is not None:
            self.push_config = m.get('PushConfig')
        return self


class SubscribeSpaceEventResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class SubscribeSpaceEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubscribeSpaceEventResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SubscribeSpaceEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncDeviceTimeRequest(TeaModel):
    def __init__(
        self,
        device_sn: str = None,
        device_time_stamp: str = None,
    ):
        self.device_sn = device_sn
        self.device_time_stamp = device_time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.device_time_stamp is not None:
            result['DeviceTimeStamp'] = self.device_time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('DeviceTimeStamp') is not None:
            self.device_time_stamp = m.get('DeviceTimeStamp')
        return self


class SyncDeviceTimeResponseBody(TeaModel):
    def __init__(
        self,
        sync_interval: str = None,
        request_id: str = None,
        message: str = None,
        retry_interval: str = None,
        ntpserver: str = None,
        code: str = None,
        time_stamp: str = None,
    ):
        self.sync_interval = sync_interval
        self.request_id = request_id
        self.message = message
        self.retry_interval = retry_interval
        self.ntpserver = ntpserver
        self.code = code
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sync_interval is not None:
            result['SyncInterval'] = self.sync_interval
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.retry_interval is not None:
            result['RetryInterval'] = self.retry_interval
        if self.ntpserver is not None:
            result['NTPServer'] = self.ntpserver
        if self.code is not None:
            result['Code'] = self.code
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SyncInterval') is not None:
            self.sync_interval = m.get('SyncInterval')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RetryInterval') is not None:
            self.retry_interval = m.get('RetryInterval')
        if m.get('NTPServer') is not None:
            self.ntpserver = m.get('NTPServer')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class SyncDeviceTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SyncDeviceTimeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SyncDeviceTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindCorpGroupRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        corp_group_id: str = None,
    ):
        self.corp_id = corp_id
        self.corp_group_id = corp_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.corp_group_id is not None:
            result['CorpGroupId'] = self.corp_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('CorpGroupId') is not None:
            self.corp_group_id = m.get('CorpGroupId')
        return self


class UnbindCorpGroupResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnbindCorpGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnbindCorpGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnbindCorpGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindPersonRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        isv_sub_id: str = None,
        profile_id: int = None,
    ):
        self.corp_id = corp_id
        self.isv_sub_id = isv_sub_id
        self.profile_id = profile_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.profile_id is not None:
            result['ProfileId'] = self.profile_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('ProfileId') is not None:
            self.profile_id = m.get('ProfileId')
        return self


class UnbindPersonResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: bool = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UnbindPersonResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnbindPersonResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnbindPersonResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindUserRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        isv_sub_id: str = None,
        user_id: int = None,
    ):
        self.corp_id = corp_id
        self.isv_sub_id = isv_sub_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UnbindUserResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: bool = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UnbindUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnbindUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnbindUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnsubscribeDeviceEventRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
    ):
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class UnsubscribeDeviceEventResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UnsubscribeDeviceEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnsubscribeDeviceEventResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnsubscribeDeviceEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnsubscribeSpaceEventRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
    ):
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class UnsubscribeSpaceEventResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UnsubscribeSpaceEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnsubscribeSpaceEventResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnsubscribeSpaceEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAiotDeviceRequestAiotDevice(TeaModel):
    def __init__(
        self,
        name: str = None,
        ipaddr: str = None,
        port: int = None,
        longitude: float = None,
        latitude: float = None,
        place: str = None,
    ):
        self.name = name
        self.ipaddr = ipaddr
        self.port = port
        self.longitude = longitude
        self.latitude = latitude
        self.place = place

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.ipaddr is not None:
            result['IPAddr'] = self.ipaddr
        if self.port is not None:
            result['Port'] = self.port
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.place is not None:
            result['Place'] = self.place
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('IPAddr') is not None:
            self.ipaddr = m.get('IPAddr')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Place') is not None:
            self.place = m.get('Place')
        return self


class UpdateAiotDeviceRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        aiot_device: UpdateAiotDeviceRequestAiotDevice = None,
    ):
        self.id = id
        self.aiot_device = aiot_device

    def validate(self):
        if self.aiot_device:
            self.aiot_device.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.aiot_device is not None:
            result['AiotDevice'] = self.aiot_device.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('AiotDevice') is not None:
            temp_model = UpdateAiotDeviceRequestAiotDevice()
            self.aiot_device = temp_model.from_map(m['AiotDevice'])
        return self


class UpdateAiotDeviceShrinkRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        aiot_device_shrink: str = None,
    ):
        self.id = id
        self.aiot_device_shrink = aiot_device_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.aiot_device_shrink is not None:
            result['AiotDevice'] = self.aiot_device_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('AiotDevice') is not None:
            self.aiot_device_shrink = m.get('AiotDevice')
        return self


class UpdateAiotDeviceResponseBodyAiotDevice(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        device_id: str = None,
        name: str = None,
        model: str = None,
        ipaddr: str = None,
        ipv6addr: str = None,
        port: int = None,
        longitude: float = None,
        latitude: float = None,
        place_code: str = None,
        place: str = None,
        org_code: str = None,
        cap_direction: str = None,
        monitor_direction: str = None,
        monitor_area_desc: str = None,
        is_online: str = None,
        owner_aps_id: str = None,
        user_id: str = None,
        password: str = None,
        mac: str = None,
        ipv_4netmask: str = None,
        ipv_4gateway: str = None,
        device_type: str = None,
        firmware_version: str = None,
        serial_number: str = None,
        manufacturer: str = None,
    ):
        self.corp_id = corp_id
        self.device_id = device_id
        self.name = name
        self.model = model
        self.ipaddr = ipaddr
        self.ipv6addr = ipv6addr
        self.port = port
        self.longitude = longitude
        self.latitude = latitude
        self.place_code = place_code
        self.place = place
        self.org_code = org_code
        self.cap_direction = cap_direction
        self.monitor_direction = monitor_direction
        self.monitor_area_desc = monitor_area_desc
        self.is_online = is_online
        self.owner_aps_id = owner_aps_id
        self.user_id = user_id
        self.password = password
        self.mac = mac
        self.ipv_4netmask = ipv_4netmask
        self.ipv_4gateway = ipv_4gateway
        self.device_type = device_type
        self.firmware_version = firmware_version
        self.serial_number = serial_number
        self.manufacturer = manufacturer

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.name is not None:
            result['Name'] = self.name
        if self.model is not None:
            result['Model'] = self.model
        if self.ipaddr is not None:
            result['IPAddr'] = self.ipaddr
        if self.ipv6addr is not None:
            result['IPV6Addr'] = self.ipv6addr
        if self.port is not None:
            result['Port'] = self.port
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.place_code is not None:
            result['PlaceCode'] = self.place_code
        if self.place is not None:
            result['Place'] = self.place
        if self.org_code is not None:
            result['OrgCode'] = self.org_code
        if self.cap_direction is not None:
            result['CapDirection'] = self.cap_direction
        if self.monitor_direction is not None:
            result['MonitorDirection'] = self.monitor_direction
        if self.monitor_area_desc is not None:
            result['MonitorAreaDesc'] = self.monitor_area_desc
        if self.is_online is not None:
            result['IsOnline'] = self.is_online
        if self.owner_aps_id is not None:
            result['OwnerApsID'] = self.owner_aps_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.password is not None:
            result['Password'] = self.password
        if self.mac is not None:
            result['MAC'] = self.mac
        if self.ipv_4netmask is not None:
            result['IPv4Netmask'] = self.ipv_4netmask
        if self.ipv_4gateway is not None:
            result['IPv4Gateway'] = self.ipv_4gateway
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.firmware_version is not None:
            result['FirmwareVersion'] = self.firmware_version
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.manufacturer is not None:
            result['Manufacturer'] = self.manufacturer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('IPAddr') is not None:
            self.ipaddr = m.get('IPAddr')
        if m.get('IPV6Addr') is not None:
            self.ipv6addr = m.get('IPV6Addr')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('PlaceCode') is not None:
            self.place_code = m.get('PlaceCode')
        if m.get('Place') is not None:
            self.place = m.get('Place')
        if m.get('OrgCode') is not None:
            self.org_code = m.get('OrgCode')
        if m.get('CapDirection') is not None:
            self.cap_direction = m.get('CapDirection')
        if m.get('MonitorDirection') is not None:
            self.monitor_direction = m.get('MonitorDirection')
        if m.get('MonitorAreaDesc') is not None:
            self.monitor_area_desc = m.get('MonitorAreaDesc')
        if m.get('IsOnline') is not None:
            self.is_online = m.get('IsOnline')
        if m.get('OwnerApsID') is not None:
            self.owner_aps_id = m.get('OwnerApsID')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('MAC') is not None:
            self.mac = m.get('MAC')
        if m.get('IPv4Netmask') is not None:
            self.ipv_4netmask = m.get('IPv4Netmask')
        if m.get('IPv4Gateway') is not None:
            self.ipv_4gateway = m.get('IPv4Gateway')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('FirmwareVersion') is not None:
            self.firmware_version = m.get('FirmwareVersion')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Manufacturer') is not None:
            self.manufacturer = m.get('Manufacturer')
        return self


class UpdateAiotDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        aiot_device: UpdateAiotDeviceResponseBodyAiotDevice = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.message = message
        self.code = code
        self.aiot_device = aiot_device

    def validate(self):
        if self.aiot_device:
            self.aiot_device.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.aiot_device is not None:
            result['AiotDevice'] = self.aiot_device.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('AiotDevice') is not None:
            temp_model = UpdateAiotDeviceResponseBodyAiotDevice()
            self.aiot_device = temp_model.from_map(m['AiotDevice'])
        return self


class UpdateAiotDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAiotDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAiotDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAiotPersonTableRequestPersonTable(TeaModel):
    def __init__(
        self,
        person_table_id: str = None,
        name: str = None,
        type: int = None,
        verification_model_list: List[int] = None,
    ):
        self.person_table_id = person_table_id
        self.name = name
        self.type = type
        self.verification_model_list = verification_model_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.person_table_id is not None:
            result['PersonTableId'] = self.person_table_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.verification_model_list is not None:
            result['VerificationModelList'] = self.verification_model_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PersonTableId') is not None:
            self.person_table_id = m.get('PersonTableId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VerificationModelList') is not None:
            self.verification_model_list = m.get('VerificationModelList')
        return self


class UpdateAiotPersonTableRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        person_table: UpdateAiotPersonTableRequestPersonTable = None,
    ):
        self.id = id
        self.person_table = person_table

    def validate(self):
        if self.person_table:
            self.person_table.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.person_table is not None:
            result['PersonTable'] = self.person_table.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PersonTable') is not None:
            temp_model = UpdateAiotPersonTableRequestPersonTable()
            self.person_table = temp_model.from_map(m['PersonTable'])
        return self


class UpdateAiotPersonTableResponseBodyPersonTable(TeaModel):
    def __init__(
        self,
        person_table_id: str = None,
        name: str = None,
        type: int = None,
        total_person_num: int = None,
        person_num: int = None,
        face_num: int = None,
        last_change: str = None,
        device_id: str = None,
        verification_model_list: List[int] = None,
    ):
        self.person_table_id = person_table_id
        self.name = name
        self.type = type
        self.total_person_num = total_person_num
        self.person_num = person_num
        self.face_num = face_num
        self.last_change = last_change
        self.device_id = device_id
        self.verification_model_list = verification_model_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.person_table_id is not None:
            result['PersonTableId'] = self.person_table_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.total_person_num is not None:
            result['TotalPersonNum'] = self.total_person_num
        if self.person_num is not None:
            result['PersonNum'] = self.person_num
        if self.face_num is not None:
            result['FaceNum'] = self.face_num
        if self.last_change is not None:
            result['LastChange'] = self.last_change
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.verification_model_list is not None:
            result['VerificationModelList'] = self.verification_model_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PersonTableId') is not None:
            self.person_table_id = m.get('PersonTableId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('TotalPersonNum') is not None:
            self.total_person_num = m.get('TotalPersonNum')
        if m.get('PersonNum') is not None:
            self.person_num = m.get('PersonNum')
        if m.get('FaceNum') is not None:
            self.face_num = m.get('FaceNum')
        if m.get('LastChange') is not None:
            self.last_change = m.get('LastChange')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('VerificationModelList') is not None:
            self.verification_model_list = m.get('VerificationModelList')
        return self


class UpdateAiotPersonTableResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        person_table: UpdateAiotPersonTableResponseBodyPersonTable = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message
        self.person_table = person_table

    def validate(self):
        if self.person_table:
            self.person_table.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.person_table is not None:
            result['PersonTable'] = self.person_table.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PersonTable') is not None:
            temp_model = UpdateAiotPersonTableResponseBodyPersonTable()
            self.person_table = temp_model.from_map(m['PersonTable'])
        return self


class UpdateAiotPersonTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAiotPersonTableResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAiotPersonTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAiotPersonTableItemRequestPersonTableItemIdentificationList(TeaModel):
    def __init__(
        self,
        type: int = None,
        number: str = None,
    ):
        self.type = type
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.number is not None:
            result['Number'] = self.number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        return self


class UpdateAiotPersonTableItemRequestPersonTableItemImageListFeatureInfo(TeaModel):
    def __init__(
        self,
        vendor: str = None,
        algorithm_version: str = None,
        algorithm_type: str = None,
        tab_ie_id: str = None,
        object_id: str = None,
        image_id: str = None,
        feature_data: str = None,
    ):
        self.vendor = vendor
        self.algorithm_version = algorithm_version
        self.algorithm_type = algorithm_type
        self.tab_ie_id = tab_ie_id
        self.object_id = object_id
        self.image_id = image_id
        self.feature_data = feature_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.algorithm_version is not None:
            result['AlgorithmVersion'] = self.algorithm_version
        if self.algorithm_type is not None:
            result['AlgorithmType'] = self.algorithm_type
        if self.tab_ie_id is not None:
            result['TabIeId'] = self.tab_ie_id
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.feature_data is not None:
            result['FeatureData'] = self.feature_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('AlgorithmVersion') is not None:
            self.algorithm_version = m.get('AlgorithmVersion')
        if m.get('AlgorithmType') is not None:
            self.algorithm_type = m.get('AlgorithmType')
        if m.get('TabIeId') is not None:
            self.tab_ie_id = m.get('TabIeId')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('FeatureData') is not None:
            self.feature_data = m.get('FeatureData')
        return self


class UpdateAiotPersonTableItemRequestPersonTableItemImageList(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        event_sort: str = None,
        device_id: str = None,
        storage_path: str = None,
        size: int = None,
        type: str = None,
        file_format: str = None,
        shot_time: str = None,
        width: int = None,
        height: int = None,
        data: str = None,
        feature_info: UpdateAiotPersonTableItemRequestPersonTableItemImageListFeatureInfo = None,
    ):
        self.image_id = image_id
        self.event_sort = event_sort
        self.device_id = device_id
        self.storage_path = storage_path
        self.size = size
        self.type = type
        self.file_format = file_format
        self.shot_time = shot_time
        self.width = width
        self.height = height
        self.data = data
        self.feature_info = feature_info

    def validate(self):
        if self.feature_info:
            self.feature_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.event_sort is not None:
            result['EventSort'] = self.event_sort
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.storage_path is not None:
            result['StoragePath'] = self.storage_path
        if self.size is not None:
            result['Size'] = self.size
        if self.type is not None:
            result['Type'] = self.type
        if self.file_format is not None:
            result['FileFormat'] = self.file_format
        if self.shot_time is not None:
            result['ShotTime'] = self.shot_time
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.data is not None:
            result['Data'] = self.data
        if self.feature_info is not None:
            result['FeatureInfo'] = self.feature_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('EventSort') is not None:
            self.event_sort = m.get('EventSort')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('StoragePath') is not None:
            self.storage_path = m.get('StoragePath')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')
        if m.get('ShotTime') is not None:
            self.shot_time = m.get('ShotTime')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('FeatureInfo') is not None:
            temp_model = UpdateAiotPersonTableItemRequestPersonTableItemImageListFeatureInfo()
            self.feature_info = temp_model.from_map(m['FeatureInfo'])
        return self


class UpdateAiotPersonTableItemRequestPersonTableItem(TeaModel):
    def __init__(
        self,
        person_id: str = None,
        person_code: str = None,
        person_name: str = None,
        remarks: str = None,
        identification_num: int = None,
        identification_list: List[UpdateAiotPersonTableItemRequestPersonTableItemIdentificationList] = None,
        image_num: int = None,
        image_list: List[UpdateAiotPersonTableItemRequestPersonTableItemImageList] = None,
    ):
        self.person_id = person_id
        self.person_code = person_code
        self.person_name = person_name
        self.remarks = remarks
        self.identification_num = identification_num
        self.identification_list = identification_list
        self.image_num = image_num
        self.image_list = image_list

    def validate(self):
        if self.identification_list:
            for k in self.identification_list:
                if k:
                    k.validate()
        if self.image_list:
            for k in self.image_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.person_code is not None:
            result['PersonCode'] = self.person_code
        if self.person_name is not None:
            result['PersonName'] = self.person_name
        if self.remarks is not None:
            result['Remarks'] = self.remarks
        if self.identification_num is not None:
            result['IdentificationNum'] = self.identification_num
        result['IdentificationList'] = []
        if self.identification_list is not None:
            for k in self.identification_list:
                result['IdentificationList'].append(k.to_map() if k else None)
        if self.image_num is not None:
            result['ImageNum'] = self.image_num
        result['ImageList'] = []
        if self.image_list is not None:
            for k in self.image_list:
                result['ImageList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('PersonCode') is not None:
            self.person_code = m.get('PersonCode')
        if m.get('PersonName') is not None:
            self.person_name = m.get('PersonName')
        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')
        if m.get('IdentificationNum') is not None:
            self.identification_num = m.get('IdentificationNum')
        self.identification_list = []
        if m.get('IdentificationList') is not None:
            for k in m.get('IdentificationList'):
                temp_model = UpdateAiotPersonTableItemRequestPersonTableItemIdentificationList()
                self.identification_list.append(temp_model.from_map(k))
        if m.get('ImageNum') is not None:
            self.image_num = m.get('ImageNum')
        self.image_list = []
        if m.get('ImageList') is not None:
            for k in m.get('ImageList'):
                temp_model = UpdateAiotPersonTableItemRequestPersonTableItemImageList()
                self.image_list.append(temp_model.from_map(k))
        return self


class UpdateAiotPersonTableItemRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        person_table_id: str = None,
        person_table_item: UpdateAiotPersonTableItemRequestPersonTableItem = None,
    ):
        self.id = id
        self.person_table_id = person_table_id
        self.person_table_item = person_table_item

    def validate(self):
        if self.person_table_item:
            self.person_table_item.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.person_table_id is not None:
            result['PersonTableId'] = self.person_table_id
        if self.person_table_item is not None:
            result['PersonTableItem'] = self.person_table_item.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PersonTableId') is not None:
            self.person_table_id = m.get('PersonTableId')
        if m.get('PersonTableItem') is not None:
            temp_model = UpdateAiotPersonTableItemRequestPersonTableItem()
            self.person_table_item = temp_model.from_map(m['PersonTableItem'])
        return self


class UpdateAiotPersonTableItemResponseBodyPersonTableItemIdentificationList(TeaModel):
    def __init__(
        self,
        type: int = None,
        number: str = None,
    ):
        self.type = type
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.number is not None:
            result['Number'] = self.number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        return self


class UpdateAiotPersonTableItemResponseBodyPersonTableItemImageListFeatureInfo(TeaModel):
    def __init__(
        self,
        vendor: str = None,
        algorithm_version: str = None,
        algorithm_type: str = None,
        tab_ied: str = None,
        object_id: str = None,
        image_id: str = None,
        feature_data: str = None,
    ):
        self.vendor = vendor
        self.algorithm_version = algorithm_version
        self.algorithm_type = algorithm_type
        self.tab_ied = tab_ied
        self.object_id = object_id
        self.image_id = image_id
        self.feature_data = feature_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.algorithm_version is not None:
            result['AlgorithmVersion'] = self.algorithm_version
        if self.algorithm_type is not None:
            result['AlgorithmType'] = self.algorithm_type
        if self.tab_ied is not None:
            result['TabIed'] = self.tab_ied
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.feature_data is not None:
            result['FeatureData'] = self.feature_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('AlgorithmVersion') is not None:
            self.algorithm_version = m.get('AlgorithmVersion')
        if m.get('AlgorithmType') is not None:
            self.algorithm_type = m.get('AlgorithmType')
        if m.get('TabIed') is not None:
            self.tab_ied = m.get('TabIed')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('FeatureData') is not None:
            self.feature_data = m.get('FeatureData')
        return self


class UpdateAiotPersonTableItemResponseBodyPersonTableItemImageList(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        event_sort: str = None,
        device_id: str = None,
        storage_path: str = None,
        size: int = None,
        type: str = None,
        file_format: str = None,
        shot_time: str = None,
        width: int = None,
        height: int = None,
        data: str = None,
        feature_info: UpdateAiotPersonTableItemResponseBodyPersonTableItemImageListFeatureInfo = None,
    ):
        self.image_id = image_id
        self.event_sort = event_sort
        self.device_id = device_id
        self.storage_path = storage_path
        self.size = size
        self.type = type
        self.file_format = file_format
        self.shot_time = shot_time
        self.width = width
        self.height = height
        self.data = data
        self.feature_info = feature_info

    def validate(self):
        if self.feature_info:
            self.feature_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.event_sort is not None:
            result['EventSort'] = self.event_sort
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.storage_path is not None:
            result['StoragePath'] = self.storage_path
        if self.size is not None:
            result['Size'] = self.size
        if self.type is not None:
            result['Type'] = self.type
        if self.file_format is not None:
            result['FileFormat'] = self.file_format
        if self.shot_time is not None:
            result['ShotTime'] = self.shot_time
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.data is not None:
            result['Data'] = self.data
        if self.feature_info is not None:
            result['FeatureInfo'] = self.feature_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('EventSort') is not None:
            self.event_sort = m.get('EventSort')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('StoragePath') is not None:
            self.storage_path = m.get('StoragePath')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')
        if m.get('ShotTime') is not None:
            self.shot_time = m.get('ShotTime')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('FeatureInfo') is not None:
            temp_model = UpdateAiotPersonTableItemResponseBodyPersonTableItemImageListFeatureInfo()
            self.feature_info = temp_model.from_map(m['FeatureInfo'])
        return self


class UpdateAiotPersonTableItemResponseBodyPersonTableItem(TeaModel):
    def __init__(
        self,
        person_table_id: str = None,
        person_id: str = None,
        last_change: str = None,
        person_code: str = None,
        person_name: str = None,
        remarks: str = None,
        identification_num: int = None,
        identification_list: List[UpdateAiotPersonTableItemResponseBodyPersonTableItemIdentificationList] = None,
        image_num: int = None,
        image_list: List[UpdateAiotPersonTableItemResponseBodyPersonTableItemImageList] = None,
    ):
        self.person_table_id = person_table_id
        self.person_id = person_id
        self.last_change = last_change
        self.person_code = person_code
        self.person_name = person_name
        self.remarks = remarks
        self.identification_num = identification_num
        self.identification_list = identification_list
        self.image_num = image_num
        self.image_list = image_list

    def validate(self):
        if self.identification_list:
            for k in self.identification_list:
                if k:
                    k.validate()
        if self.image_list:
            for k in self.image_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.person_table_id is not None:
            result['PersonTableId'] = self.person_table_id
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        if self.last_change is not None:
            result['LastChange'] = self.last_change
        if self.person_code is not None:
            result['PersonCode'] = self.person_code
        if self.person_name is not None:
            result['PersonName'] = self.person_name
        if self.remarks is not None:
            result['Remarks'] = self.remarks
        if self.identification_num is not None:
            result['IdentificationNum'] = self.identification_num
        result['IdentificationList'] = []
        if self.identification_list is not None:
            for k in self.identification_list:
                result['IdentificationList'].append(k.to_map() if k else None)
        if self.image_num is not None:
            result['ImageNum'] = self.image_num
        result['ImageList'] = []
        if self.image_list is not None:
            for k in self.image_list:
                result['ImageList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PersonTableId') is not None:
            self.person_table_id = m.get('PersonTableId')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        if m.get('LastChange') is not None:
            self.last_change = m.get('LastChange')
        if m.get('PersonCode') is not None:
            self.person_code = m.get('PersonCode')
        if m.get('PersonName') is not None:
            self.person_name = m.get('PersonName')
        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')
        if m.get('IdentificationNum') is not None:
            self.identification_num = m.get('IdentificationNum')
        self.identification_list = []
        if m.get('IdentificationList') is not None:
            for k in m.get('IdentificationList'):
                temp_model = UpdateAiotPersonTableItemResponseBodyPersonTableItemIdentificationList()
                self.identification_list.append(temp_model.from_map(k))
        if m.get('ImageNum') is not None:
            self.image_num = m.get('ImageNum')
        self.image_list = []
        if m.get('ImageList') is not None:
            for k in m.get('ImageList'):
                temp_model = UpdateAiotPersonTableItemResponseBodyPersonTableItemImageList()
                self.image_list.append(temp_model.from_map(k))
        return self


class UpdateAiotPersonTableItemResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        person_table_item: UpdateAiotPersonTableItemResponseBodyPersonTableItem = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.message = message
        self.code = code
        self.person_table_item = person_table_item

    def validate(self):
        if self.person_table_item:
            self.person_table_item.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.person_table_item is not None:
            result['PersonTableItem'] = self.person_table_item.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('PersonTableItem') is not None:
            temp_model = UpdateAiotPersonTableItemResponseBodyPersonTableItem()
            self.person_table_item = temp_model.from_map(m['PersonTableItem'])
        return self


class UpdateAiotPersonTableItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAiotPersonTableItemResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAiotPersonTableItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCorpRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        corp_name: str = None,
        app_name: str = None,
        parent_corp_id: str = None,
        description: str = None,
        isv_sub_id: str = None,
        icon_path: str = None,
    ):
        self.corp_id = corp_id
        self.corp_name = corp_name
        self.app_name = app_name
        self.parent_corp_id = parent_corp_id
        self.description = description
        self.isv_sub_id = isv_sub_id
        self.icon_path = icon_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.corp_name is not None:
            result['CorpName'] = self.corp_name
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.parent_corp_id is not None:
            result['ParentCorpId'] = self.parent_corp_id
        if self.description is not None:
            result['Description'] = self.description
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.icon_path is not None:
            result['IconPath'] = self.icon_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('CorpName') is not None:
            self.corp_name = m.get('CorpName')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ParentCorpId') is not None:
            self.parent_corp_id = m.get('ParentCorpId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('IconPath') is not None:
            self.icon_path = m.get('IconPath')
        return self


class UpdateCorpResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UpdateCorpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateCorpResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateCorpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDeviceRequest(TeaModel):
    def __init__(
        self,
        gb_id: str = None,
        device_name: str = None,
        device_type: str = None,
        device_address: str = None,
        device_site: str = None,
        device_direction: str = None,
        device_resolution: str = None,
        bit_rate: str = None,
        corp_id: str = None,
        vendor: str = None,
    ):
        self.gb_id = gb_id
        self.device_name = device_name
        self.device_type = device_type
        self.device_address = device_address
        self.device_site = device_site
        self.device_direction = device_direction
        self.device_resolution = device_resolution
        self.bit_rate = bit_rate
        self.corp_id = corp_id
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.device_address is not None:
            result['DeviceAddress'] = self.device_address
        if self.device_site is not None:
            result['DeviceSite'] = self.device_site
        if self.device_direction is not None:
            result['DeviceDirection'] = self.device_direction
        if self.device_resolution is not None:
            result['DeviceResolution'] = self.device_resolution
        if self.bit_rate is not None:
            result['BitRate'] = self.bit_rate
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('DeviceAddress') is not None:
            self.device_address = m.get('DeviceAddress')
        if m.get('DeviceSite') is not None:
            self.device_site = m.get('DeviceSite')
        if m.get('DeviceDirection') is not None:
            self.device_direction = m.get('DeviceDirection')
        if m.get('DeviceResolution') is not None:
            self.device_resolution = m.get('DeviceResolution')
        if m.get('BitRate') is not None:
            self.bit_rate = m.get('BitRate')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class UpdateDeviceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UpdateDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDeviceCaptureStrategyRequest(TeaModel):
    def __init__(
        self,
        device_type: str = None,
        device_code: str = None,
        monday_capture_strategy: str = None,
    ):
        # 设备类型
        self.device_type = device_type
        # 设备通道
        self.device_code = device_code
        # 周一图片抓去模式
        self.monday_capture_strategy = monday_capture_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.device_code is not None:
            result['DeviceCode'] = self.device_code
        if self.monday_capture_strategy is not None:
            result['MondayCaptureStrategy'] = self.monday_capture_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('DeviceCode') is not None:
            self.device_code = m.get('DeviceCode')
        if m.get('MondayCaptureStrategy') is not None:
            self.monday_capture_strategy = m.get('MondayCaptureStrategy')
        return self


class UpdateDeviceCaptureStrategyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        # RequestId
        self.request_id = request_id
        # 响应码
        self.code = code
        # 响应信息
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class UpdateDeviceCaptureStrategyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDeviceCaptureStrategyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateDeviceCaptureStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDoubleVerificationGroupRequestDoubleVerificationGroupPersonIdList(TeaModel):
    def __init__(
        self,
        person_table_id: str = None,
        person_id: str = None,
    ):
        self.person_table_id = person_table_id
        self.person_id = person_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.person_table_id is not None:
            result['PersonTableId'] = self.person_table_id
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PersonTableId') is not None:
            self.person_table_id = m.get('PersonTableId')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        return self


class UpdateDoubleVerificationGroupRequestDoubleVerificationGroup(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        interval: int = None,
        member_number: int = None,
        person_id_list: List[UpdateDoubleVerificationGroupRequestDoubleVerificationGroupPersonIdList] = None,
    ):
        self.group_id = group_id
        self.interval = interval
        self.member_number = member_number
        self.person_id_list = person_id_list

    def validate(self):
        if self.person_id_list:
            for k in self.person_id_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.member_number is not None:
            result['MemberNumber'] = self.member_number
        result['PersonIdList'] = []
        if self.person_id_list is not None:
            for k in self.person_id_list:
                result['PersonIdList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('MemberNumber') is not None:
            self.member_number = m.get('MemberNumber')
        self.person_id_list = []
        if m.get('PersonIdList') is not None:
            for k in m.get('PersonIdList'):
                temp_model = UpdateDoubleVerificationGroupRequestDoubleVerificationGroupPersonIdList()
                self.person_id_list.append(temp_model.from_map(k))
        return self


class UpdateDoubleVerificationGroupRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        double_verification_group: UpdateDoubleVerificationGroupRequestDoubleVerificationGroup = None,
    ):
        self.id = id
        self.double_verification_group = double_verification_group

    def validate(self):
        if self.double_verification_group:
            self.double_verification_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.double_verification_group is not None:
            result['DoubleVerificationGroup'] = self.double_verification_group.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('DoubleVerificationGroup') is not None:
            temp_model = UpdateDoubleVerificationGroupRequestDoubleVerificationGroup()
            self.double_verification_group = temp_model.from_map(m['DoubleVerificationGroup'])
        return self


class UpdateDoubleVerificationGroupResponseBodyDoubleVerificationGroupPersonIdList(TeaModel):
    def __init__(
        self,
        person_table_id: str = None,
        person_id: str = None,
    ):
        self.person_table_id = person_table_id
        self.person_id = person_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.person_table_id is not None:
            result['PersonTableId'] = self.person_table_id
        if self.person_id is not None:
            result['PersonId'] = self.person_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PersonTableId') is not None:
            self.person_table_id = m.get('PersonTableId')
        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')
        return self


class UpdateDoubleVerificationGroupResponseBodyDoubleVerificationGroup(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        interval: int = None,
        last_change: str = None,
        member_number: int = None,
        person_id_list: List[UpdateDoubleVerificationGroupResponseBodyDoubleVerificationGroupPersonIdList] = None,
        enabled: str = None,
        device_id: str = None,
    ):
        self.group_id = group_id
        self.interval = interval
        self.last_change = last_change
        self.member_number = member_number
        self.person_id_list = person_id_list
        self.enabled = enabled
        self.device_id = device_id

    def validate(self):
        if self.person_id_list:
            for k in self.person_id_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.last_change is not None:
            result['LastChange'] = self.last_change
        if self.member_number is not None:
            result['MemberNumber'] = self.member_number
        result['PersonIdList'] = []
        if self.person_id_list is not None:
            for k in self.person_id_list:
                result['PersonIdList'].append(k.to_map() if k else None)
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('LastChange') is not None:
            self.last_change = m.get('LastChange')
        if m.get('MemberNumber') is not None:
            self.member_number = m.get('MemberNumber')
        self.person_id_list = []
        if m.get('PersonIdList') is not None:
            for k in m.get('PersonIdList'):
                temp_model = UpdateDoubleVerificationGroupResponseBodyDoubleVerificationGroupPersonIdList()
                self.person_id_list.append(temp_model.from_map(k))
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class UpdateDoubleVerificationGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        double_verification_group: UpdateDoubleVerificationGroupResponseBodyDoubleVerificationGroup = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message
        self.double_verification_group = double_verification_group

    def validate(self):
        if self.double_verification_group:
            self.double_verification_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.double_verification_group is not None:
            result['DoubleVerificationGroup'] = self.double_verification_group.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DoubleVerificationGroup') is not None:
            temp_model = UpdateDoubleVerificationGroupResponseBodyDoubleVerificationGroup()
            self.double_verification_group = temp_model.from_map(m['DoubleVerificationGroup'])
        return self


class UpdateDoubleVerificationGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDoubleVerificationGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateDoubleVerificationGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMarkerRequest(TeaModel):
    def __init__(
        self,
        algorithm_id: str = None,
        label_id: str = None,
        sample_id: str = None,
        content: str = None,
        marker_id: str = None,
    ):
        self.algorithm_id = algorithm_id
        self.label_id = label_id
        self.sample_id = sample_id
        self.content = content
        self.marker_id = marker_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        if self.sample_id is not None:
            result['SampleId'] = self.sample_id
        if self.content is not None:
            result['Content'] = self.content
        if self.marker_id is not None:
            result['MarkerId'] = self.marker_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        if m.get('SampleId') is not None:
            self.sample_id = m.get('SampleId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('MarkerId') is not None:
            self.marker_id = m.get('MarkerId')
        return self


class UpdateMarkerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class UpdateMarkerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateMarkerResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateMarkerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMonitorRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        task_id: str = None,
        rule_name: str = None,
        device_operate_type: str = None,
        device_list: str = None,
        pic_operate_type: str = None,
        pic_list: str = None,
        attribute_operate_type: str = None,
        attribute_name: str = None,
        attribute_value_list: str = None,
        description: str = None,
        rule_expression: str = None,
        algorithm_vendor: str = None,
        notifier_type: str = None,
        notifier_url: str = None,
        notifier_app_secret: str = None,
        notifier_time_out: int = None,
        notifier_extend_values: str = None,
    ):
        self.corp_id = corp_id
        self.task_id = task_id
        self.rule_name = rule_name
        self.device_operate_type = device_operate_type
        self.device_list = device_list
        self.pic_operate_type = pic_operate_type
        self.pic_list = pic_list
        self.attribute_operate_type = attribute_operate_type
        self.attribute_name = attribute_name
        self.attribute_value_list = attribute_value_list
        self.description = description
        self.rule_expression = rule_expression
        self.algorithm_vendor = algorithm_vendor
        self.notifier_type = notifier_type
        self.notifier_url = notifier_url
        self.notifier_app_secret = notifier_app_secret
        self.notifier_time_out = notifier_time_out
        self.notifier_extend_values = notifier_extend_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.device_operate_type is not None:
            result['DeviceOperateType'] = self.device_operate_type
        if self.device_list is not None:
            result['DeviceList'] = self.device_list
        if self.pic_operate_type is not None:
            result['PicOperateType'] = self.pic_operate_type
        if self.pic_list is not None:
            result['PicList'] = self.pic_list
        if self.attribute_operate_type is not None:
            result['AttributeOperateType'] = self.attribute_operate_type
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name
        if self.attribute_value_list is not None:
            result['AttributeValueList'] = self.attribute_value_list
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_expression is not None:
            result['RuleExpression'] = self.rule_expression
        if self.algorithm_vendor is not None:
            result['AlgorithmVendor'] = self.algorithm_vendor
        if self.notifier_type is not None:
            result['NotifierType'] = self.notifier_type
        if self.notifier_url is not None:
            result['NotifierUrl'] = self.notifier_url
        if self.notifier_app_secret is not None:
            result['NotifierAppSecret'] = self.notifier_app_secret
        if self.notifier_time_out is not None:
            result['NotifierTimeOut'] = self.notifier_time_out
        if self.notifier_extend_values is not None:
            result['NotifierExtendValues'] = self.notifier_extend_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('DeviceOperateType') is not None:
            self.device_operate_type = m.get('DeviceOperateType')
        if m.get('DeviceList') is not None:
            self.device_list = m.get('DeviceList')
        if m.get('PicOperateType') is not None:
            self.pic_operate_type = m.get('PicOperateType')
        if m.get('PicList') is not None:
            self.pic_list = m.get('PicList')
        if m.get('AttributeOperateType') is not None:
            self.attribute_operate_type = m.get('AttributeOperateType')
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')
        if m.get('AttributeValueList') is not None:
            self.attribute_value_list = m.get('AttributeValueList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleExpression') is not None:
            self.rule_expression = m.get('RuleExpression')
        if m.get('AlgorithmVendor') is not None:
            self.algorithm_vendor = m.get('AlgorithmVendor')
        if m.get('NotifierType') is not None:
            self.notifier_type = m.get('NotifierType')
        if m.get('NotifierUrl') is not None:
            self.notifier_url = m.get('NotifierUrl')
        if m.get('NotifierAppSecret') is not None:
            self.notifier_app_secret = m.get('NotifierAppSecret')
        if m.get('NotifierTimeOut') is not None:
            self.notifier_time_out = m.get('NotifierTimeOut')
        if m.get('NotifierExtendValues') is not None:
            self.notifier_extend_values = m.get('NotifierExtendValues')
        return self


class UpdateMonitorResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UpdateMonitorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateMonitorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProfileRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        isv_sub_id: str = None,
        name: str = None,
        catalog_id: int = None,
        id_number: str = None,
        face_url: str = None,
        live_address: str = None,
        gender: int = None,
        plate_no: str = None,
        phone_no: str = None,
        scene_type: str = None,
        biz_id: str = None,
        profile_id: int = None,
    ):
        self.corp_id = corp_id
        self.isv_sub_id = isv_sub_id
        self.name = name
        self.catalog_id = catalog_id
        self.id_number = id_number
        self.face_url = face_url
        self.live_address = live_address
        self.gender = gender
        self.plate_no = plate_no
        self.phone_no = phone_no
        self.scene_type = scene_type
        self.biz_id = biz_id
        self.profile_id = profile_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.name is not None:
            result['Name'] = self.name
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.id_number is not None:
            result['IdNumber'] = self.id_number
        if self.face_url is not None:
            result['FaceUrl'] = self.face_url
        if self.live_address is not None:
            result['LiveAddress'] = self.live_address
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.plate_no is not None:
            result['PlateNo'] = self.plate_no
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.profile_id is not None:
            result['ProfileId'] = self.profile_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('IdNumber') is not None:
            self.id_number = m.get('IdNumber')
        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')
        if m.get('LiveAddress') is not None:
            self.live_address = m.get('LiveAddress')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('PlateNo') is not None:
            self.plate_no = m.get('PlateNo')
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ProfileId') is not None:
            self.profile_id = m.get('ProfileId')
        return self


class UpdateProfileResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UpdateProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateProfileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProfileCatalogRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        isv_sub_id: str = None,
        catalog_id: int = None,
        catalog_name: str = None,
    ):
        self.corp_id = corp_id
        self.isv_sub_id = isv_sub_id
        self.catalog_id = catalog_id
        self.catalog_name = catalog_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        return self


class UpdateProfileCatalogResponseBodyData(TeaModel):
    def __init__(
        self,
        catalog_id: int = None,
        catalog_name: str = None,
        isv_sub_id: str = None,
        parent_catalog_id: str = None,
        profile_count: int = None,
    ):
        self.catalog_id = catalog_id
        self.catalog_name = catalog_name
        self.isv_sub_id = isv_sub_id
        self.parent_catalog_id = parent_catalog_id
        self.profile_count = profile_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.parent_catalog_id is not None:
            result['ParentCatalogId'] = self.parent_catalog_id
        if self.profile_count is not None:
            result['ProfileCount'] = self.profile_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('ParentCatalogId') is not None:
            self.parent_catalog_id = m.get('ParentCatalogId')
        if m.get('ProfileCount') is not None:
            self.profile_count = m.get('ProfileCount')
        return self


class UpdateProfileCatalogResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: UpdateProfileCatalogResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = UpdateProfileCatalogResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UpdateProfileCatalogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateProfileCatalogResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateProfileCatalogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSampleRequest(TeaModel):
    def __init__(
        self,
        algorithm_id: str = None,
        sample_id: str = None,
        label_id: str = None,
    ):
        self.algorithm_id = algorithm_id
        self.sample_id = sample_id
        self.label_id = label_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.sample_id is not None:
            result['SampleId'] = self.sample_id
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('SampleId') is not None:
            self.sample_id = m.get('SampleId')
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        return self


class UpdateSampleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        label_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.label_id = label_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        return self


class UpdateSampleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateSampleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateSampleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTrainAlgorithmRequest(TeaModel):
    def __init__(
        self,
        algorithm_id: str = None,
        algorithm_name: str = None,
    ):
        self.algorithm_id = algorithm_id
        self.algorithm_name = algorithm_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        return self


class UpdateTrainAlgorithmResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class UpdateTrainAlgorithmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateTrainAlgorithmResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateTrainAlgorithmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTrainLabelRequest(TeaModel):
    def __init__(
        self,
        label_id: str = None,
        label_name: str = None,
    ):
        self.label_id = label_id
        self.label_name = label_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        if self.label_name is not None:
            result['LabelName'] = self.label_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        if m.get('LabelName') is not None:
            self.label_name = m.get('LabelName')
        return self


class UpdateTrainLabelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class UpdateTrainLabelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateTrainLabelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateTrainLabelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        isv_sub_id: str = None,
        user_name: str = None,
        user_group_id: int = None,
        id_number: str = None,
        face_image_url: str = None,
        face_image_content: str = None,
        address: str = None,
        age: int = None,
        gender: int = None,
        plate_no: str = None,
        phone_no: str = None,
        attachment: str = None,
        biz_id: str = None,
        user_id: int = None,
    ):
        self.corp_id = corp_id
        self.isv_sub_id = isv_sub_id
        self.user_name = user_name
        self.user_group_id = user_group_id
        self.id_number = id_number
        self.face_image_url = face_image_url
        self.face_image_content = face_image_content
        self.address = address
        self.age = age
        self.gender = gender
        self.plate_no = plate_no
        self.phone_no = phone_no
        self.attachment = attachment
        self.biz_id = biz_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.id_number is not None:
            result['IdNumber'] = self.id_number
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.face_image_content is not None:
            result['FaceImageContent'] = self.face_image_content
        if self.address is not None:
            result['Address'] = self.address
        if self.age is not None:
            result['Age'] = self.age
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.plate_no is not None:
            result['PlateNo'] = self.plate_no
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        if self.attachment is not None:
            result['Attachment'] = self.attachment
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('IdNumber') is not None:
            self.id_number = m.get('IdNumber')
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('FaceImageContent') is not None:
            self.face_image_content = m.get('FaceImageContent')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('PlateNo') is not None:
            self.plate_no = m.get('PlateNo')
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        if m.get('Attachment') is not None:
            self.attachment = m.get('Attachment')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UpdateUserResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UpdateUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserGroupRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        isv_sub_id: str = None,
        user_group_id: int = None,
        user_group_name: str = None,
    ):
        self.corp_id = corp_id
        self.isv_sub_id = isv_sub_id
        self.user_group_id = user_group_id
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        return self


class UpdateUserGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        isv_sub_id: str = None,
        user_group_id: int = None,
        user_group_name: str = None,
        user_count: int = None,
        parent_user_group_id: str = None,
    ):
        self.isv_sub_id = isv_sub_id
        self.user_group_id = user_group_id
        self.user_group_name = user_group_name
        self.user_count = user_count
        self.parent_user_group_id = parent_user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isv_sub_id is not None:
            result['IsvSubId'] = self.isv_sub_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        if self.user_count is not None:
            result['UserCount'] = self.user_count
        if self.parent_user_group_id is not None:
            result['ParentUserGroupId'] = self.parent_user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsvSubId') is not None:
            self.isv_sub_id = m.get('IsvSubId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')
        if m.get('ParentUserGroupId') is not None:
            self.parent_user_group_id = m.get('ParentUserGroupId')
        return self


class UpdateUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: UpdateUserGroupResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = UpdateUserGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UpdateUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateUserGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadFileRequest(TeaModel):
    def __init__(
        self,
        file_type: str = None,
        md5: str = None,
        corp_id: str = None,
        file_content: str = None,
        file_name: str = None,
        file_alias_name: str = None,
        data_source_id: str = None,
        file_path: str = None,
    ):
        self.file_type = file_type
        self.md5 = md5
        self.corp_id = corp_id
        self.file_content = file_content
        self.file_name = file_name
        self.file_alias_name = file_alias_name
        self.data_source_id = data_source_id
        self.file_path = file_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.md5 is not None:
            result['MD5'] = self.md5
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.file_content is not None:
            result['FileContent'] = self.file_content
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_alias_name is not None:
            result['FileAliasName'] = self.file_alias_name
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('MD5') is not None:
            self.md5 = m.get('MD5')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('FileContent') is not None:
            self.file_content = m.get('FileContent')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileAliasName') is not None:
            self.file_alias_name = m.get('FileAliasName')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        return self


class UploadFileResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        oss_path: str = None,
        source_id: str = None,
    ):
        self.oss_path = oss_path
        self.source_id = source_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        return self


class UploadFileResponseBodyData(TeaModel):
    def __init__(
        self,
        records: List[UploadFileResponseBodyDataRecords] = None,
    ):
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = UploadFileResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        return self


class UploadFileResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: UploadFileResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = UploadFileResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UploadFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UploadFileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UploadFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadImageRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
    ):
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        return self


class UploadImageResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UploadImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UploadImageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UploadImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyDeviceRequest(TeaModel):
    def __init__(
        self,
        city_code: str = None,
        file_path: str = None,
    ):
        # 城市编码
        self.city_code = city_code
        # OSS路径
        self.file_path = file_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city_code is not None:
            result['CityCode'] = self.city_code
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        return self


class VerifyDeviceResponseBodyData(TeaModel):
    def __init__(
        self,
        original_gb_id: str = None,
        suggest_gb_id: str = None,
        message: str = None,
        code: str = None,
        row_number: int = None,
        id: str = None,
    ):
        # 原始国标编码
        self.original_gb_id = original_gb_id
        # 建议的国标编码
        self.suggest_gb_id = suggest_gb_id
        # 格式错误或国标冲突提示
        self.message = message
        # 格式错误或国标冲突的错误码，0为成功，-1为失败
        self.code = code
        # 记录所在行号
        self.row_number = row_number
        # Excel中的序号列的值
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.original_gb_id is not None:
            result['OriginalGbId'] = self.original_gb_id
        if self.suggest_gb_id is not None:
            result['SuggestGbId'] = self.suggest_gb_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.row_number is not None:
            result['RowNumber'] = self.row_number
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginalGbId') is not None:
            self.original_gb_id = m.get('OriginalGbId')
        if m.get('SuggestGbId') is not None:
            self.suggest_gb_id = m.get('SuggestGbId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RowNumber') is not None:
            self.row_number = m.get('RowNumber')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class VerifyDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        data: List[VerifyDeviceResponseBodyData] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 响应码描述
        self.message = message
        # 响应码
        self.code = code
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = VerifyDeviceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class VerifyDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: VerifyDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = VerifyDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyTrainLabelRequest(TeaModel):
    def __init__(
        self,
        algorithm_id: str = None,
        label_name: str = None,
    ):
        self.algorithm_id = algorithm_id
        self.label_name = label_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id
        if self.label_name is not None:
            result['LabelName'] = self.label_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')
        if m.get('LabelName') is not None:
            self.label_name = m.get('LabelName')
        return self


class VerifyTrainLabelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class VerifyTrainLabelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: VerifyTrainLabelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = VerifyTrainLabelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


