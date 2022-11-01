# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import BinaryIO, Dict, List


class AddImageRequest(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        crop: bool = None,
        custom_content: str = None,
        instance_name: str = None,
        int_attr: int = None,
        pic_content: str = None,
        pic_name: str = None,
        product_id: str = None,
        region: str = None,
        str_attr: str = None,
    ):
        self.category_id = category_id
        self.crop = crop
        self.custom_content = custom_content
        self.instance_name = instance_name
        self.int_attr = int_attr
        self.pic_content = pic_content
        self.pic_name = pic_name
        self.product_id = product_id
        self.region = region
        self.str_attr = str_attr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.pic_content is not None:
            result['PicContent'] = self.pic_content
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.region is not None:
            result['Region'] = self.region
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('PicContent') is not None:
            self.pic_content = m.get('PicContent')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        return self


class AddImageAdvanceRequest(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        crop: bool = None,
        custom_content: str = None,
        instance_name: str = None,
        int_attr: int = None,
        pic_content_object: BinaryIO = None,
        pic_name: str = None,
        product_id: str = None,
        region: str = None,
        str_attr: str = None,
    ):
        self.category_id = category_id
        self.crop = crop
        self.custom_content = custom_content
        self.instance_name = instance_name
        self.int_attr = int_attr
        self.pic_content_object = pic_content_object
        self.pic_name = pic_name
        self.product_id = product_id
        self.region = region
        self.str_attr = str_attr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.pic_content_object is not None:
            result['PicContent'] = self.pic_content_object
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.region is not None:
            result['Region'] = self.region
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('PicContent') is not None:
            self.pic_content_object = m.get('PicContent')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        return self


class AddImageResponseBodyPicInfo(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        region: str = None,
    ):
        self.category_id = category_id
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class AddImageResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        pic_info: AddImageResponseBodyPicInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.pic_info = pic_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.pic_info:
            self.pic_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.pic_info is not None:
            result['PicInfo'] = self.pic_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PicInfo') is not None:
            temp_model = AddImageResponseBodyPicInfo()
            self.pic_info = temp_model.from_map(m['PicInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImageRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        pic_name: str = None,
        product_id: str = None,
    ):
        self.instance_name = instance_name
        self.pic_name = pic_name
        self.product_id = product_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        return self


class DeleteImageResponseBodyData(TeaModel):
    def __init__(
        self,
        pic_names: List[str] = None,
    ):
        self.pic_names = pic_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_names is not None:
            result['PicNames'] = self.pic_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicNames') is not None:
            self.pic_names = m.get('PicNames')
        return self


class DeleteImageResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DeleteImageResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeleteImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetailRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
    ):
        self.instance_name = instance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class DetailResponseBodyInstance(TeaModel):
    def __init__(
        self,
        capacity: int = None,
        name: str = None,
        qps: int = None,
        region: str = None,
        service_type: int = None,
        total_count: int = None,
        utc_create: str = None,
        utc_expire_time: str = None,
    ):
        self.capacity = capacity
        self.name = name
        self.qps = qps
        self.region = region
        self.service_type = service_type
        self.total_count = total_count
        self.utc_create = utc_create
        self.utc_expire_time = utc_expire_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.name is not None:
            result['Name'] = self.name
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.region is not None:
            result['Region'] = self.region
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.utc_create is not None:
            result['UtcCreate'] = self.utc_create
        if self.utc_expire_time is not None:
            result['UtcExpireTime'] = self.utc_expire_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('UtcCreate') is not None:
            self.utc_create = m.get('UtcCreate')
        if m.get('UtcExpireTime') is not None:
            self.utc_expire_time = m.get('UtcExpireTime')
        return self


class DetailResponseBody(TeaModel):
    def __init__(
        self,
        instance: DetailResponseBodyInstance = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.instance = instance
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instance') is not None:
            temp_model = DetailResponseBodyInstance()
            self.instance = temp_model.from_map(m['Instance'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DumpMetaRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
    ):
        self.instance_name = instance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class DumpMetaResponseBodyData(TeaModel):
    def __init__(
        self,
        dump_meta_status: str = None,
        id: str = None,
    ):
        self.dump_meta_status = dump_meta_status
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dump_meta_status is not None:
            result['DumpMetaStatus'] = self.dump_meta_status
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DumpMetaStatus') is not None:
            self.dump_meta_status = m.get('DumpMetaStatus')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DumpMetaResponseBody(TeaModel):
    def __init__(
        self,
        data: DumpMetaResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.request_id = request_id
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DumpMetaResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DumpMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DumpMetaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DumpMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DumpMetaListRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        instance_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.id = id
        self.instance_name = instance_name
        self.page_number = page_number
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
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DumpMetaListResponseBodyDataDumpMetaList(TeaModel):
    def __init__(
        self,
        code: str = None,
        id: int = None,
        meta_url: str = None,
        msg: str = None,
        status: str = None,
        utc_create: str = None,
        utc_modified: int = None,
    ):
        self.code = code
        self.id = id
        self.meta_url = meta_url
        self.msg = msg
        self.status = status
        self.utc_create = utc_create
        self.utc_modified = utc_modified

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.id is not None:
            result['Id'] = self.id
        if self.meta_url is not None:
            result['MetaUrl'] = self.meta_url
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.status is not None:
            result['Status'] = self.status
        if self.utc_create is not None:
            result['UtcCreate'] = self.utc_create
        if self.utc_modified is not None:
            result['UtcModified'] = self.utc_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MetaUrl') is not None:
            self.meta_url = m.get('MetaUrl')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UtcCreate') is not None:
            self.utc_create = m.get('UtcCreate')
        if m.get('UtcModified') is not None:
            self.utc_modified = m.get('UtcModified')
        return self


class DumpMetaListResponseBodyData(TeaModel):
    def __init__(
        self,
        dump_meta_list: List[DumpMetaListResponseBodyDataDumpMetaList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.dump_meta_list = dump_meta_list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.dump_meta_list:
            for k in self.dump_meta_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DumpMetaList'] = []
        if self.dump_meta_list is not None:
            for k in self.dump_meta_list:
                result['DumpMetaList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dump_meta_list = []
        if m.get('DumpMetaList') is not None:
            for k in m.get('DumpMetaList'):
                temp_model = DumpMetaListResponseBodyDataDumpMetaList()
                self.dump_meta_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DumpMetaListResponseBody(TeaModel):
    def __init__(
        self,
        data: DumpMetaListResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DumpMetaListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DumpMetaListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DumpMetaListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DumpMetaListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IncreaseInstanceRequest(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        callback_address: str = None,
        instance_name: str = None,
        path: str = None,
    ):
        self.bucket_name = bucket_name
        self.callback_address = callback_address
        self.instance_name = instance_name
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.callback_address is not None:
            result['CallbackAddress'] = self.callback_address
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('CallbackAddress') is not None:
            self.callback_address = m.get('CallbackAddress')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class IncreaseInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
        increment_status: str = None,
    ):
        self.id = id
        self.increment_status = increment_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.increment_status is not None:
            result['IncrementStatus'] = self.increment_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncrementStatus') is not None:
            self.increment_status = m.get('IncrementStatus')
        return self


class IncreaseInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: IncreaseInstanceResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.request_id = request_id
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = IncreaseInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class IncreaseInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IncreaseInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = IncreaseInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IncreaseListRequest(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        id: int = None,
        instance_name: str = None,
        page_number: int = None,
        page_size: int = None,
        path: str = None,
    ):
        self.bucket_name = bucket_name
        self.id = id
        self.instance_name = instance_name
        self.page_number = page_number
        self.page_size = page_size
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class IncreaseListResponseBodyDataIncrementsInstance(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        callback_address: str = None,
        code: str = None,
        error_url: str = None,
        id: int = None,
        msg: str = None,
        path: str = None,
        status: str = None,
        utc_create: str = None,
        utc_modified: int = None,
    ):
        self.bucket_name = bucket_name
        self.callback_address = callback_address
        self.code = code
        self.error_url = error_url
        self.id = id
        self.msg = msg
        self.path = path
        self.status = status
        self.utc_create = utc_create
        self.utc_modified = utc_modified

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.callback_address is not None:
            result['CallbackAddress'] = self.callback_address
        if self.code is not None:
            result['Code'] = self.code
        if self.error_url is not None:
            result['ErrorUrl'] = self.error_url
        if self.id is not None:
            result['Id'] = self.id
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.path is not None:
            result['Path'] = self.path
        if self.status is not None:
            result['Status'] = self.status
        if self.utc_create is not None:
            result['UtcCreate'] = self.utc_create
        if self.utc_modified is not None:
            result['UtcModified'] = self.utc_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('CallbackAddress') is not None:
            self.callback_address = m.get('CallbackAddress')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorUrl') is not None:
            self.error_url = m.get('ErrorUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UtcCreate') is not None:
            self.utc_create = m.get('UtcCreate')
        if m.get('UtcModified') is not None:
            self.utc_modified = m.get('UtcModified')
        return self


class IncreaseListResponseBodyDataIncrements(TeaModel):
    def __init__(
        self,
        instance: List[IncreaseListResponseBodyDataIncrementsInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = IncreaseListResponseBodyDataIncrementsInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class IncreaseListResponseBodyData(TeaModel):
    def __init__(
        self,
        increments: IncreaseListResponseBodyDataIncrements = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.increments = increments
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.increments:
            self.increments.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.increments is not None:
            result['Increments'] = self.increments.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Increments') is not None:
            temp_model = IncreaseListResponseBodyDataIncrements()
            self.increments = temp_model.from_map(m['Increments'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class IncreaseListResponseBody(TeaModel):
    def __init__(
        self,
        data: IncreaseListResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = IncreaseListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class IncreaseListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IncreaseListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = IncreaseListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchImageByNameRequest(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        filter: str = None,
        instance_name: str = None,
        num: int = None,
        pic_name: str = None,
        product_id: str = None,
        start: int = None,
    ):
        self.category_id = category_id
        self.filter = filter
        self.instance_name = instance_name
        self.num = num
        self.pic_name = pic_name
        self.product_id = product_id
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.num is not None:
            result['Num'] = self.num
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class SearchImageByNameResponseBodyAuctions(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        custom_content: str = None,
        int_attr: int = None,
        pic_name: str = None,
        product_id: str = None,
        score: float = None,
        sort_expr_values: str = None,
        str_attr: str = None,
    ):
        self.category_id = category_id
        self.custom_content = custom_content
        self.int_attr = int_attr
        self.pic_name = pic_name
        self.product_id = product_id
        self.score = score
        self.sort_expr_values = sort_expr_values
        self.str_attr = str_attr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.score is not None:
            result['Score'] = self.score
        if self.sort_expr_values is not None:
            result['SortExprValues'] = self.sort_expr_values
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('SortExprValues') is not None:
            self.sort_expr_values = m.get('SortExprValues')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        return self


class SearchImageByNameResponseBodyHead(TeaModel):
    def __init__(
        self,
        docs_found: int = None,
        docs_return: int = None,
        search_time: int = None,
    ):
        self.docs_found = docs_found
        self.docs_return = docs_return
        self.search_time = search_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.docs_found is not None:
            result['DocsFound'] = self.docs_found
        if self.docs_return is not None:
            result['DocsReturn'] = self.docs_return
        if self.search_time is not None:
            result['SearchTime'] = self.search_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocsFound') is not None:
            self.docs_found = m.get('DocsFound')
        if m.get('DocsReturn') is not None:
            self.docs_return = m.get('DocsReturn')
        if m.get('SearchTime') is not None:
            self.search_time = m.get('SearchTime')
        return self


class SearchImageByNameResponseBodyPicInfoAllCategories(TeaModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class SearchImageByNameResponseBodyPicInfoMultiRegion(TeaModel):
    def __init__(
        self,
        region: str = None,
    ):
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class SearchImageByNameResponseBodyPicInfo(TeaModel):
    def __init__(
        self,
        all_categories: List[SearchImageByNameResponseBodyPicInfoAllCategories] = None,
        category_id: int = None,
        multi_region: List[SearchImageByNameResponseBodyPicInfoMultiRegion] = None,
        region: str = None,
    ):
        self.all_categories = all_categories
        self.category_id = category_id
        self.multi_region = multi_region
        self.region = region

    def validate(self):
        if self.all_categories:
            for k in self.all_categories:
                if k:
                    k.validate()
        if self.multi_region:
            for k in self.multi_region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AllCategories'] = []
        if self.all_categories is not None:
            for k in self.all_categories:
                result['AllCategories'].append(k.to_map() if k else None)
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        result['MultiRegion'] = []
        if self.multi_region is not None:
            for k in self.multi_region:
                result['MultiRegion'].append(k.to_map() if k else None)
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.all_categories = []
        if m.get('AllCategories') is not None:
            for k in m.get('AllCategories'):
                temp_model = SearchImageByNameResponseBodyPicInfoAllCategories()
                self.all_categories.append(temp_model.from_map(k))
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        self.multi_region = []
        if m.get('MultiRegion') is not None:
            for k in m.get('MultiRegion'):
                temp_model = SearchImageByNameResponseBodyPicInfoMultiRegion()
                self.multi_region.append(temp_model.from_map(k))
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class SearchImageByNameResponseBody(TeaModel):
    def __init__(
        self,
        auctions: List[SearchImageByNameResponseBodyAuctions] = None,
        code: int = None,
        head: SearchImageByNameResponseBodyHead = None,
        msg: str = None,
        pic_info: SearchImageByNameResponseBodyPicInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.auctions = auctions
        self.code = code
        self.head = head
        self.msg = msg
        self.pic_info = pic_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.auctions:
            for k in self.auctions:
                if k:
                    k.validate()
        if self.head:
            self.head.validate()
        if self.pic_info:
            self.pic_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Auctions'] = []
        if self.auctions is not None:
            for k in self.auctions:
                result['Auctions'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.head is not None:
            result['Head'] = self.head.to_map()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.pic_info is not None:
            result['PicInfo'] = self.pic_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auctions = []
        if m.get('Auctions') is not None:
            for k in m.get('Auctions'):
                temp_model = SearchImageByNameResponseBodyAuctions()
                self.auctions.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Head') is not None:
            temp_model = SearchImageByNameResponseBodyHead()
            self.head = temp_model.from_map(m['Head'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('PicInfo') is not None:
            temp_model = SearchImageByNameResponseBodyPicInfo()
            self.pic_info = temp_model.from_map(m['PicInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchImageByNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchImageByNameResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SearchImageByNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchImageByPicRequest(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        crop: bool = None,
        filter: str = None,
        instance_name: str = None,
        num: int = None,
        pic_content: str = None,
        region: str = None,
        start: int = None,
    ):
        self.category_id = category_id
        self.crop = crop
        self.filter = filter
        self.instance_name = instance_name
        self.num = num
        self.pic_content = pic_content
        self.region = region
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.num is not None:
            result['Num'] = self.num
        if self.pic_content is not None:
            result['PicContent'] = self.pic_content
        if self.region is not None:
            result['Region'] = self.region
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('PicContent') is not None:
            self.pic_content = m.get('PicContent')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class SearchImageByPicAdvanceRequest(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        crop: bool = None,
        filter: str = None,
        instance_name: str = None,
        num: int = None,
        pic_content_object: BinaryIO = None,
        region: str = None,
        start: int = None,
    ):
        self.category_id = category_id
        self.crop = crop
        self.filter = filter
        self.instance_name = instance_name
        self.num = num
        self.pic_content_object = pic_content_object
        self.region = region
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.num is not None:
            result['Num'] = self.num
        if self.pic_content_object is not None:
            result['PicContent'] = self.pic_content_object
        if self.region is not None:
            result['Region'] = self.region
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('PicContent') is not None:
            self.pic_content_object = m.get('PicContent')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class SearchImageByPicResponseBodyAuctions(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        custom_content: str = None,
        int_attr: int = None,
        pic_name: str = None,
        product_id: str = None,
        score: float = None,
        sort_expr_values: str = None,
        str_attr: str = None,
    ):
        self.category_id = category_id
        self.custom_content = custom_content
        self.int_attr = int_attr
        self.pic_name = pic_name
        self.product_id = product_id
        self.score = score
        self.sort_expr_values = sort_expr_values
        self.str_attr = str_attr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.score is not None:
            result['Score'] = self.score
        if self.sort_expr_values is not None:
            result['SortExprValues'] = self.sort_expr_values
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('SortExprValues') is not None:
            self.sort_expr_values = m.get('SortExprValues')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        return self


class SearchImageByPicResponseBodyHead(TeaModel):
    def __init__(
        self,
        docs_found: int = None,
        docs_return: int = None,
        search_time: int = None,
    ):
        self.docs_found = docs_found
        self.docs_return = docs_return
        self.search_time = search_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.docs_found is not None:
            result['DocsFound'] = self.docs_found
        if self.docs_return is not None:
            result['DocsReturn'] = self.docs_return
        if self.search_time is not None:
            result['SearchTime'] = self.search_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocsFound') is not None:
            self.docs_found = m.get('DocsFound')
        if m.get('DocsReturn') is not None:
            self.docs_return = m.get('DocsReturn')
        if m.get('SearchTime') is not None:
            self.search_time = m.get('SearchTime')
        return self


class SearchImageByPicResponseBodyPicInfoAllCategories(TeaModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class SearchImageByPicResponseBodyPicInfoMultiRegion(TeaModel):
    def __init__(
        self,
        region: str = None,
    ):
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class SearchImageByPicResponseBodyPicInfo(TeaModel):
    def __init__(
        self,
        all_categories: List[SearchImageByPicResponseBodyPicInfoAllCategories] = None,
        category_id: int = None,
        multi_region: List[SearchImageByPicResponseBodyPicInfoMultiRegion] = None,
        region: str = None,
    ):
        self.all_categories = all_categories
        self.category_id = category_id
        self.multi_region = multi_region
        self.region = region

    def validate(self):
        if self.all_categories:
            for k in self.all_categories:
                if k:
                    k.validate()
        if self.multi_region:
            for k in self.multi_region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AllCategories'] = []
        if self.all_categories is not None:
            for k in self.all_categories:
                result['AllCategories'].append(k.to_map() if k else None)
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        result['MultiRegion'] = []
        if self.multi_region is not None:
            for k in self.multi_region:
                result['MultiRegion'].append(k.to_map() if k else None)
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.all_categories = []
        if m.get('AllCategories') is not None:
            for k in m.get('AllCategories'):
                temp_model = SearchImageByPicResponseBodyPicInfoAllCategories()
                self.all_categories.append(temp_model.from_map(k))
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        self.multi_region = []
        if m.get('MultiRegion') is not None:
            for k in m.get('MultiRegion'):
                temp_model = SearchImageByPicResponseBodyPicInfoMultiRegion()
                self.multi_region.append(temp_model.from_map(k))
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class SearchImageByPicResponseBody(TeaModel):
    def __init__(
        self,
        auctions: List[SearchImageByPicResponseBodyAuctions] = None,
        code: int = None,
        head: SearchImageByPicResponseBodyHead = None,
        msg: str = None,
        pic_info: SearchImageByPicResponseBodyPicInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.auctions = auctions
        self.code = code
        self.head = head
        self.msg = msg
        self.pic_info = pic_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.auctions:
            for k in self.auctions:
                if k:
                    k.validate()
        if self.head:
            self.head.validate()
        if self.pic_info:
            self.pic_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Auctions'] = []
        if self.auctions is not None:
            for k in self.auctions:
                result['Auctions'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.head is not None:
            result['Head'] = self.head.to_map()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.pic_info is not None:
            result['PicInfo'] = self.pic_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auctions = []
        if m.get('Auctions') is not None:
            for k in m.get('Auctions'):
                temp_model = SearchImageByPicResponseBodyAuctions()
                self.auctions.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Head') is not None:
            temp_model = SearchImageByPicResponseBodyHead()
            self.head = temp_model.from_map(m['Head'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('PicInfo') is not None:
            temp_model = SearchImageByPicResponseBodyPicInfo()
            self.pic_info = temp_model.from_map(m['PicInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchImageByPicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchImageByPicResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SearchImageByPicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateImageRequest(TeaModel):
    def __init__(
        self,
        custom_content: str = None,
        instance_name: str = None,
        int_attr: int = None,
        pic_name: str = None,
        product_id: str = None,
        str_attr: str = None,
    ):
        self.custom_content = custom_content
        self.instance_name = instance_name
        self.int_attr = int_attr
        self.pic_name = pic_name
        self.product_id = product_id
        self.str_attr = str_attr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        return self


class UpdateImageResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


