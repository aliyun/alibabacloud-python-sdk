# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, BinaryIO


class DescribeWhitelistSettingRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        service_code: str = None,
        scene_id: int = None,
        certify_id: str = None,
        cert_no: str = None,
        valid_start_date: int = None,
        valid_end_date: int = None,
        status: str = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.service_code = service_code
        self.scene_id = scene_id
        self.certify_id = certify_id
        self.cert_no = cert_no
        self.valid_start_date = valid_start_date
        self.valid_end_date = valid_end_date
        self.status = status
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        self.validate_required(self.service_code, 'service_code')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.current_page, 'current_page')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.valid_start_date is not None:
            result['ValidStartDate'] = self.valid_start_date
        if self.valid_end_date is not None:
            result['ValidEndDate'] = self.valid_end_date
        if self.status is not None:
            result['Status'] = self.status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('ValidStartDate') is not None:
            self.valid_start_date = m.get('ValidStartDate')
        if m.get('ValidEndDate') is not None:
            self.valid_end_date = m.get('ValidEndDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class DescribeWhitelistSettingResponseItems(TeaModel):
    def __init__(
        self,
        id: int = None,
        scene_id: int = None,
        valid_start_date: str = None,
        valid_end_date: str = None,
        cert_no: str = None,
        certify_id: str = None,
        status: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
    ):
        self.id = id
        self.scene_id = scene_id
        self.valid_start_date = valid_start_date
        self.valid_end_date = valid_end_date
        self.cert_no = cert_no
        self.certify_id = certify_id
        self.status = status
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.scene_id, 'scene_id')
        self.validate_required(self.valid_start_date, 'valid_start_date')
        self.validate_required(self.valid_end_date, 'valid_end_date')
        self.validate_required(self.cert_no, 'cert_no')
        self.validate_required(self.certify_id, 'certify_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.gmt_create, 'gmt_create')
        self.validate_required(self.gmt_modified, 'gmt_modified')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.valid_start_date is not None:
            result['ValidStartDate'] = self.valid_start_date
        if self.valid_end_date is not None:
            result['ValidEndDate'] = self.valid_end_date
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.status is not None:
            result['Status'] = self.status
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('ValidStartDate') is not None:
            self.valid_start_date = m.get('ValidStartDate')
        if m.get('ValidEndDate') is not None:
            self.valid_end_date = m.get('ValidEndDate')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        return self


class DescribeWhitelistSettingResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        current_page: int = None,
        page_size: int = None,
        items: List[DescribeWhitelistSettingResponseItems] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.current_page = current_page
        self.page_size = page_size
        self.items = items

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.current_page, 'current_page')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.items, 'items')
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeWhitelistSettingResponseItems()
                self.items.append(temp_model.from_map(k))
        return self


class DeleteWhitelistSettingRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        service_code: str = None,
        ids: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.service_code = service_code
        self.ids = ids

    def validate(self):
        self.validate_required(self.service_code, 'service_code')
        self.validate_required(self.ids, 'ids')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.ids is not None:
            result['Ids'] = self.ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        return self


class DeleteWhitelistSettingResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: bool = None,
    ):
        self.request_id = request_id
        self.result_object = result_object

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.result_object, 'result_object')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_object is not None:
            result['ResultObject'] = self.result_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            self.result_object = m.get('ResultObject')
        return self


class CreateWhitelistSettingRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        service_code: str = None,
        scene_id: int = None,
        certify_id: str = None,
        cert_no: str = None,
        valid_day: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.service_code = service_code
        self.scene_id = scene_id
        self.certify_id = certify_id
        self.cert_no = cert_no
        self.valid_day = valid_day

    def validate(self):
        self.validate_required(self.service_code, 'service_code')
        self.validate_required(self.valid_day, 'valid_day')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.valid_day is not None:
            result['ValidDay'] = self.valid_day
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('ValidDay') is not None:
            self.valid_day = m.get('ValidDay')
        return self


class CreateWhitelistSettingResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: bool = None,
    ):
        self.request_id = request_id
        self.result_object = result_object

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.result_object, 'result_object')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_object is not None:
            result['ResultObject'] = self.result_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            self.result_object = m.get('ResultObject')
        return self


class DescribeWhitelistRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_type: str = None,
        biz_id: str = None,
        id_card_num: str = None,
        valid_start_date: str = None,
        valid_end_date: str = None,
        valid: str = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_type = biz_type
        self.biz_id = biz_id
        self.id_card_num = id_card_num
        self.valid_start_date = valid_start_date
        self.valid_end_date = valid_end_date
        self.valid = valid
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.current_page, 'current_page')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.id_card_num is not None:
            result['IdCardNum'] = self.id_card_num
        if self.valid_start_date is not None:
            result['ValidStartDate'] = self.valid_start_date
        if self.valid_end_date is not None:
            result['ValidEndDate'] = self.valid_end_date
        if self.valid is not None:
            result['Valid'] = self.valid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('IdCardNum') is not None:
            self.id_card_num = m.get('IdCardNum')
        if m.get('ValidStartDate') is not None:
            self.valid_start_date = m.get('ValidStartDate')
        if m.get('ValidEndDate') is not None:
            self.valid_end_date = m.get('ValidEndDate')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class DescribeWhitelistResponseItems(TeaModel):
    def __init__(
        self,
        id: int = None,
        uid: int = None,
        biz_type: str = None,
        start_date: int = None,
        end_date: int = None,
        id_card_num: str = None,
        biz_id: str = None,
        valid: int = None,
        gmt_create: int = None,
        gmt_modified: int = None,
    ):
        self.id = id
        self.uid = uid
        self.biz_type = biz_type
        self.start_date = start_date
        self.end_date = end_date
        self.id_card_num = id_card_num
        self.biz_id = biz_id
        self.valid = valid
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.uid, 'uid')
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')
        self.validate_required(self.id_card_num, 'id_card_num')
        self.validate_required(self.biz_id, 'biz_id')
        self.validate_required(self.valid, 'valid')
        self.validate_required(self.gmt_create, 'gmt_create')
        self.validate_required(self.gmt_modified, 'gmt_modified')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.id_card_num is not None:
            result['IdCardNum'] = self.id_card_num
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.valid is not None:
            result['Valid'] = self.valid
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('IdCardNum') is not None:
            self.id_card_num = m.get('IdCardNum')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        return self


class DescribeWhitelistResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        current_page: int = None,
        page_size: int = None,
        items: List[DescribeWhitelistResponseItems] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.current_page = current_page
        self.page_size = page_size
        self.items = items

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.current_page, 'current_page')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.items, 'items')
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeWhitelistResponseItems()
                self.items.append(temp_model.from_map(k))
        return self


class DeleteWhitelistRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        ids: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.ids = ids

    def validate(self):
        self.validate_required(self.ids, 'ids')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.ids is not None:
            result['Ids'] = self.ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        return self


class DeleteWhitelistResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateWhitelistRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_type: str = None,
        biz_id: str = None,
        id_card_num: str = None,
        valid_day: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_type = biz_type
        self.biz_id = biz_id
        self.id_card_num = id_card_num
        self.valid_day = valid_day

    def validate(self):
        self.validate_required(self.biz_id, 'biz_id')
        self.validate_required(self.id_card_num, 'id_card_num')
        self.validate_required(self.valid_day, 'valid_day')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.id_card_num is not None:
            result['IdCardNum'] = self.id_card_num
        if self.valid_day is not None:
            result['ValidDay'] = self.valid_day
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('IdCardNum') is not None:
            self.id_card_num = m.get('IdCardNum')
        if m.get('ValidDay') is not None:
            self.valid_day = m.get('ValidDay')
        return self


class CreateWhitelistResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFaceConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeFaceConfigResponseItems(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        biz_name: str = None,
        gmt_updated: int = None,
    ):
        self.biz_type = biz_type
        self.biz_name = biz_name
        self.gmt_updated = gmt_updated

    def validate(self):
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.biz_name, 'biz_name')
        self.validate_required(self.gmt_updated, 'gmt_updated')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.gmt_updated is not None:
            result['GmtUpdated'] = self.gmt_updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('GmtUpdated') is not None:
            self.gmt_updated = m.get('GmtUpdated')
        return self


class DescribeFaceConfigResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        items: List[DescribeFaceConfigResponseItems] = None,
    ):
        self.request_id = request_id
        self.items = items

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.items, 'items')
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeFaceConfigResponseItems()
                self.items.append(temp_model.from_map(k))
        return self


class UpdateFaceConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_type: str = None,
        biz_name: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_type = biz_type
        self.biz_name = biz_name

    def validate(self):
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.biz_name, 'biz_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        return self


class UpdateFaceConfigResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFaceConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        biz_type: str = None,
        biz_name: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.biz_type = biz_type
        self.biz_name = biz_name

    def validate(self):
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.biz_name, 'biz_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        return self


class CreateFaceConfigResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class LivenessFaceVerifyRequest(TeaModel):
    def __init__(
        self,
        scene_id: int = None,
        outer_order_no: str = None,
        product_code: str = None,
        face_contrast_picture: str = None,
        device_token: str = None,
        mobile: str = None,
        ip: str = None,
        user_id: str = None,
        face_contrast_picture_url: str = None,
        certify_id: str = None,
        oss_bucket_name: str = None,
        oss_object_name: str = None,
        model: str = None,
        crop: str = None,
    ):
        self.scene_id = scene_id
        self.outer_order_no = outer_order_no
        self.product_code = product_code
        self.face_contrast_picture = face_contrast_picture
        self.device_token = device_token
        self.mobile = mobile
        self.ip = ip
        self.user_id = user_id
        self.face_contrast_picture_url = face_contrast_picture_url
        self.certify_id = certify_id
        self.oss_bucket_name = oss_bucket_name
        self.oss_object_name = oss_object_name
        self.model = model
        self.crop = crop

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.face_contrast_picture is not None:
            result['FaceContrastPicture'] = self.face_contrast_picture
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.face_contrast_picture_url is not None:
            result['FaceContrastPictureUrl'] = self.face_contrast_picture_url
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name
        if self.model is not None:
            result['Model'] = self.model
        if self.crop is not None:
            result['Crop'] = self.crop
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('FaceContrastPicture') is not None:
            self.face_contrast_picture = m.get('FaceContrastPicture')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('FaceContrastPictureUrl') is not None:
            self.face_contrast_picture_url = m.get('FaceContrastPictureUrl')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        return self


class LivenessFaceVerifyResponseResultObject(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
        sub_code: str = None,
        material_info: str = None,
        passed: str = None,
    ):
        self.certify_id = certify_id
        self.sub_code = sub_code
        self.material_info = material_info
        self.passed = passed

    def validate(self):
        self.validate_required(self.certify_id, 'certify_id')
        self.validate_required(self.sub_code, 'sub_code')
        self.validate_required(self.material_info, 'material_info')
        self.validate_required(self.passed, 'passed')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info
        if self.passed is not None:
            result['Passed'] = self.passed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        return self


class LivenessFaceVerifyResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: LivenessFaceVerifyResponseResultObject = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result_object = result_object

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = LivenessFaceVerifyResponseResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class CompareFaceVerifyRequest(TeaModel):
    def __init__(
        self,
        scene_id: int = None,
        outer_order_no: str = None,
        product_code: str = None,
        source_face_contrast_picture: str = None,
        source_face_contrast_picture_url: str = None,
        source_certify_id: str = None,
        source_oss_bucket_name: str = None,
        source_oss_object_name: str = None,
        target_face_contrast_picture: str = None,
        target_face_contrast_picture_url: str = None,
        target_certify_id: str = None,
        target_oss_bucket_name: str = None,
        target_oss_object_name: str = None,
        crop: str = None,
    ):
        self.scene_id = scene_id
        self.outer_order_no = outer_order_no
        self.product_code = product_code
        self.source_face_contrast_picture = source_face_contrast_picture
        self.source_face_contrast_picture_url = source_face_contrast_picture_url
        self.source_certify_id = source_certify_id
        self.source_oss_bucket_name = source_oss_bucket_name
        self.source_oss_object_name = source_oss_object_name
        self.target_face_contrast_picture = target_face_contrast_picture
        self.target_face_contrast_picture_url = target_face_contrast_picture_url
        self.target_certify_id = target_certify_id
        self.target_oss_bucket_name = target_oss_bucket_name
        self.target_oss_object_name = target_oss_object_name
        self.crop = crop

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.source_face_contrast_picture is not None:
            result['SourceFaceContrastPicture'] = self.source_face_contrast_picture
        if self.source_face_contrast_picture_url is not None:
            result['SourceFaceContrastPictureUrl'] = self.source_face_contrast_picture_url
        if self.source_certify_id is not None:
            result['SourceCertifyId'] = self.source_certify_id
        if self.source_oss_bucket_name is not None:
            result['SourceOssBucketName'] = self.source_oss_bucket_name
        if self.source_oss_object_name is not None:
            result['SourceOssObjectName'] = self.source_oss_object_name
        if self.target_face_contrast_picture is not None:
            result['TargetFaceContrastPicture'] = self.target_face_contrast_picture
        if self.target_face_contrast_picture_url is not None:
            result['TargetFaceContrastPictureUrl'] = self.target_face_contrast_picture_url
        if self.target_certify_id is not None:
            result['TargetCertifyId'] = self.target_certify_id
        if self.target_oss_bucket_name is not None:
            result['TargetOssBucketName'] = self.target_oss_bucket_name
        if self.target_oss_object_name is not None:
            result['TargetOssObjectName'] = self.target_oss_object_name
        if self.crop is not None:
            result['Crop'] = self.crop
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('SourceFaceContrastPicture') is not None:
            self.source_face_contrast_picture = m.get('SourceFaceContrastPicture')
        if m.get('SourceFaceContrastPictureUrl') is not None:
            self.source_face_contrast_picture_url = m.get('SourceFaceContrastPictureUrl')
        if m.get('SourceCertifyId') is not None:
            self.source_certify_id = m.get('SourceCertifyId')
        if m.get('SourceOssBucketName') is not None:
            self.source_oss_bucket_name = m.get('SourceOssBucketName')
        if m.get('SourceOssObjectName') is not None:
            self.source_oss_object_name = m.get('SourceOssObjectName')
        if m.get('TargetFaceContrastPicture') is not None:
            self.target_face_contrast_picture = m.get('TargetFaceContrastPicture')
        if m.get('TargetFaceContrastPictureUrl') is not None:
            self.target_face_contrast_picture_url = m.get('TargetFaceContrastPictureUrl')
        if m.get('TargetCertifyId') is not None:
            self.target_certify_id = m.get('TargetCertifyId')
        if m.get('TargetOssBucketName') is not None:
            self.target_oss_bucket_name = m.get('TargetOssBucketName')
        if m.get('TargetOssObjectName') is not None:
            self.target_oss_object_name = m.get('TargetOssObjectName')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        return self


class CompareFaceVerifyResponseResultObject(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
        verify_score: float = None,
        passed: str = None,
    ):
        self.certify_id = certify_id
        self.verify_score = verify_score
        self.passed = passed

    def validate(self):
        self.validate_required(self.certify_id, 'certify_id')
        self.validate_required(self.verify_score, 'verify_score')
        self.validate_required(self.passed, 'passed')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.verify_score is not None:
            result['VerifyScore'] = self.verify_score
        if self.passed is not None:
            result['Passed'] = self.passed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('VerifyScore') is not None:
            self.verify_score = m.get('VerifyScore')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        return self


class CompareFaceVerifyResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: CompareFaceVerifyResponseResultObject = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result_object = result_object

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = CompareFaceVerifyResponseResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class DescribeSdkUrlRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        debug: bool = None,
    ):
        self.id = id
        self.debug = debug

    def validate(self):
        self.validate_required(self.id, 'id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.debug is not None:
            result['Debug'] = self.debug
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Debug') is not None:
            self.debug = m.get('Debug')
        return self


class DescribeSdkUrlResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sdk_url: str = None,
    ):
        self.request_id = request_id
        self.sdk_url = sdk_url

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.sdk_url, 'sdk_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sdk_url is not None:
            result['SdkUrl'] = self.sdk_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SdkUrl') is not None:
            self.sdk_url = m.get('SdkUrl')
        return self


class DescribeUpdatePackageResultRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        self.validate_required(self.task_id, 'task_id')

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


class DescribeUpdatePackageResultResponseAppInfoPackageInfo(TeaModel):
    def __init__(
        self,
        version: str = None,
    ):
        self.version = version

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeUpdatePackageResultResponseAppInfoDebugPackageInfo(TeaModel):
    def __init__(
        self,
        version: str = None,
    ):
        self.version = version

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeUpdatePackageResultResponseAppInfo(TeaModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        package_name: str = None,
        icon: str = None,
        start_date: str = None,
        end_date: str = None,
        type: int = None,
        package_info: DescribeUpdatePackageResultResponseAppInfoPackageInfo = None,
        debug_package_info: DescribeUpdatePackageResultResponseAppInfoDebugPackageInfo = None,
    ):
        self.id = id
        self.name = name
        self.package_name = package_name
        self.icon = icon
        self.start_date = start_date
        self.end_date = end_date
        self.type = type
        self.package_info = package_info
        self.debug_package_info = debug_package_info

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.package_name, 'package_name')
        self.validate_required(self.icon, 'icon')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')
        self.validate_required(self.type, 'type')
        self.validate_required(self.package_info, 'package_info')
        if self.package_info:
            self.package_info.validate()
        self.validate_required(self.debug_package_info, 'debug_package_info')
        if self.debug_package_info:
            self.debug_package_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.type is not None:
            result['Type'] = self.type
        if self.package_info is not None:
            result['PackageInfo'] = self.package_info.to_map()
        if self.debug_package_info is not None:
            result['DebugPackageInfo'] = self.debug_package_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('PackageInfo') is not None:
            temp_model = DescribeUpdatePackageResultResponseAppInfoPackageInfo()
            self.package_info = temp_model.from_map(m['PackageInfo'])
        if m.get('DebugPackageInfo') is not None:
            temp_model = DescribeUpdatePackageResultResponseAppInfoDebugPackageInfo()
            self.debug_package_info = temp_model.from_map(m['DebugPackageInfo'])
        return self


class DescribeUpdatePackageResultResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        app_info: DescribeUpdatePackageResultResponseAppInfo = None,
    ):
        self.request_id = request_id
        self.app_info = app_info

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.app_info, 'app_info')
        if self.app_info:
            self.app_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.app_info is not None:
            result['AppInfo'] = self.app_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AppInfo') is not None:
            temp_model = DescribeUpdatePackageResultResponseAppInfo()
            self.app_info = temp_model.from_map(m['AppInfo'])
        return self


class UpdateAppPackageRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        package_url: str = None,
        platform: str = None,
        debug: bool = None,
    ):
        self.id = id
        self.package_url = package_url
        self.platform = platform
        self.debug = debug

    def validate(self):
        self.validate_required(self.package_url, 'package_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.package_url is not None:
            result['PackageUrl'] = self.package_url
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.debug is not None:
            result['Debug'] = self.debug
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Debug') is not None:
            self.debug = m.get('Debug')
        return self


class UpdateAppPackageResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeAppInfoRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        current_page: int = None,
        platform: str = None,
    ):
        self.page_size = page_size
        self.current_page = current_page
        self.platform = platform

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.platform is not None:
            result['Platform'] = self.platform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        return self


class DescribeAppInfoResponseAppInfoListPackageInfo(TeaModel):
    def __init__(
        self,
        version: str = None,
    ):
        self.version = version

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeAppInfoResponseAppInfoListDebugPackageInfo(TeaModel):
    def __init__(
        self,
        version: str = None,
    ):
        self.version = version

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeAppInfoResponseAppInfoList(TeaModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        package_name: str = None,
        icon: str = None,
        start_date: str = None,
        end_date: str = None,
        type: int = None,
        package_info: DescribeAppInfoResponseAppInfoListPackageInfo = None,
        debug_package_info: DescribeAppInfoResponseAppInfoListDebugPackageInfo = None,
    ):
        self.id = id
        self.name = name
        self.package_name = package_name
        self.icon = icon
        self.start_date = start_date
        self.end_date = end_date
        self.type = type
        self.package_info = package_info
        self.debug_package_info = debug_package_info

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.package_name, 'package_name')
        self.validate_required(self.icon, 'icon')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')
        self.validate_required(self.type, 'type')
        self.validate_required(self.package_info, 'package_info')
        if self.package_info:
            self.package_info.validate()
        self.validate_required(self.debug_package_info, 'debug_package_info')
        if self.debug_package_info:
            self.debug_package_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.type is not None:
            result['Type'] = self.type
        if self.package_info is not None:
            result['PackageInfo'] = self.package_info.to_map()
        if self.debug_package_info is not None:
            result['DebugPackageInfo'] = self.debug_package_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('PackageInfo') is not None:
            temp_model = DescribeAppInfoResponseAppInfoListPackageInfo()
            self.package_info = temp_model.from_map(m['PackageInfo'])
        if m.get('DebugPackageInfo') is not None:
            temp_model = DescribeAppInfoResponseAppInfoListDebugPackageInfo()
            self.debug_package_info = temp_model.from_map(m['DebugPackageInfo'])
        return self


class DescribeAppInfoResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_size: int = None,
        current_page: int = None,
        total_count: int = None,
        app_info_list: List[DescribeAppInfoResponseAppInfoList] = None,
    ):
        self.request_id = request_id
        self.page_size = page_size
        self.current_page = current_page
        self.total_count = total_count
        self.app_info_list = app_info_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.current_page, 'current_page')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.app_info_list, 'app_info_list')
        if self.app_info_list:
            for k in self.app_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['AppInfoList'] = []
        if self.app_info_list is not None:
            for k in self.app_info_list:
                result['AppInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.app_info_list = []
        if m.get('AppInfoList') is not None:
            for k in m.get('AppInfoList'):
                temp_model = DescribeAppInfoResponseAppInfoList()
                self.app_info_list.append(temp_model.from_map(k))
        return self


class ContrastFaceVerifyRequest(TeaModel):
    def __init__(
        self,
        scene_id: int = None,
        outer_order_no: str = None,
        product_code: str = None,
        cert_type: str = None,
        cert_name: str = None,
        cert_no: str = None,
        face_contrast_picture: str = None,
        device_token: str = None,
        mobile: str = None,
        ip: str = None,
        user_id: str = None,
        face_contrast_picture_url: str = None,
        certify_id: str = None,
        oss_bucket_name: str = None,
        oss_object_name: str = None,
        model: str = None,
        face_contrast_file: str = None,
        crop: str = None,
    ):
        self.scene_id = scene_id
        self.outer_order_no = outer_order_no
        self.product_code = product_code
        self.cert_type = cert_type
        self.cert_name = cert_name
        self.cert_no = cert_no
        self.face_contrast_picture = face_contrast_picture
        self.device_token = device_token
        self.mobile = mobile
        self.ip = ip
        self.user_id = user_id
        self.face_contrast_picture_url = face_contrast_picture_url
        self.certify_id = certify_id
        self.oss_bucket_name = oss_bucket_name
        self.oss_object_name = oss_object_name
        self.model = model
        self.face_contrast_file = face_contrast_file
        self.crop = crop

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.face_contrast_picture is not None:
            result['FaceContrastPicture'] = self.face_contrast_picture
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.face_contrast_picture_url is not None:
            result['FaceContrastPictureUrl'] = self.face_contrast_picture_url
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name
        if self.model is not None:
            result['Model'] = self.model
        if self.face_contrast_file is not None:
            result['FaceContrastFile'] = self.face_contrast_file
        if self.crop is not None:
            result['Crop'] = self.crop
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('FaceContrastPicture') is not None:
            self.face_contrast_picture = m.get('FaceContrastPicture')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('FaceContrastPictureUrl') is not None:
            self.face_contrast_picture_url = m.get('FaceContrastPictureUrl')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('FaceContrastFile') is not None:
            self.face_contrast_file = m.get('FaceContrastFile')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        return self


class ContrastFaceVerifyResponseResultObject(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
        sub_code: str = None,
        material_info: str = None,
        identity_info: str = None,
        passed: str = None,
    ):
        self.certify_id = certify_id
        self.sub_code = sub_code
        self.material_info = material_info
        self.identity_info = identity_info
        self.passed = passed

    def validate(self):
        self.validate_required(self.certify_id, 'certify_id')
        self.validate_required(self.sub_code, 'sub_code')
        self.validate_required(self.material_info, 'material_info')
        self.validate_required(self.identity_info, 'identity_info')
        self.validate_required(self.passed, 'passed')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info
        if self.identity_info is not None:
            result['IdentityInfo'] = self.identity_info
        if self.passed is not None:
            result['Passed'] = self.passed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')
        if m.get('IdentityInfo') is not None:
            self.identity_info = m.get('IdentityInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        return self


class ContrastFaceVerifyResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: ContrastFaceVerifyResponseResultObject = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result_object = result_object

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = ContrastFaceVerifyResponseResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class ContrastFaceVerifyAdvanceRequest(TeaModel):
    def __init__(
        self,
        face_contrast_file_object: BinaryIO = None,
        scene_id: int = None,
        outer_order_no: str = None,
        product_code: str = None,
        cert_type: str = None,
        cert_name: str = None,
        cert_no: str = None,
        face_contrast_picture: str = None,
        device_token: str = None,
        mobile: str = None,
        ip: str = None,
        user_id: str = None,
        face_contrast_picture_url: str = None,
        certify_id: str = None,
        oss_bucket_name: str = None,
        oss_object_name: str = None,
        model: str = None,
        crop: str = None,
    ):
        self.face_contrast_file_object = face_contrast_file_object
        self.scene_id = scene_id
        self.outer_order_no = outer_order_no
        self.product_code = product_code
        self.cert_type = cert_type
        self.cert_name = cert_name
        self.cert_no = cert_no
        self.face_contrast_picture = face_contrast_picture
        self.device_token = device_token
        self.mobile = mobile
        self.ip = ip
        self.user_id = user_id
        self.face_contrast_picture_url = face_contrast_picture_url
        self.certify_id = certify_id
        self.oss_bucket_name = oss_bucket_name
        self.oss_object_name = oss_object_name
        self.model = model
        self.crop = crop

    def validate(self):
        self.validate_required(self.face_contrast_file_object, 'face_contrast_file_object')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_contrast_file_object is not None:
            result['FaceContrastFileObject'] = self.face_contrast_file_object
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.face_contrast_picture is not None:
            result['FaceContrastPicture'] = self.face_contrast_picture
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.face_contrast_picture_url is not None:
            result['FaceContrastPictureUrl'] = self.face_contrast_picture_url
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name
        if self.model is not None:
            result['Model'] = self.model
        if self.crop is not None:
            result['Crop'] = self.crop
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceContrastFileObject') is not None:
            self.face_contrast_file_object = m.get('FaceContrastFileObject')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('FaceContrastPicture') is not None:
            self.face_contrast_picture = m.get('FaceContrastPicture')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('FaceContrastPictureUrl') is not None:
            self.face_contrast_picture_url = m.get('FaceContrastPictureUrl')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        return self


class InitDeviceRequest(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
        outer_order_no: str = None,
        channel: str = None,
        merchant: str = None,
        product_name: str = None,
        produce_node: str = None,
        biz_data: str = None,
        meta_info: str = None,
        certify_principal: str = None,
        app_version: str = None,
        device_token: str = None,
        ua_token: str = None,
        web_umid_token: str = None,
    ):
        self.certify_id = certify_id
        self.outer_order_no = outer_order_no
        self.channel = channel
        self.merchant = merchant
        self.product_name = product_name
        self.produce_node = produce_node
        self.biz_data = biz_data
        self.meta_info = meta_info
        self.certify_principal = certify_principal
        self.app_version = app_version
        self.device_token = device_token
        self.ua_token = ua_token
        self.web_umid_token = web_umid_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.merchant is not None:
            result['Merchant'] = self.merchant
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.produce_node is not None:
            result['ProduceNode'] = self.produce_node
        if self.biz_data is not None:
            result['BizData'] = self.biz_data
        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info
        if self.certify_principal is not None:
            result['CertifyPrincipal'] = self.certify_principal
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.ua_token is not None:
            result['UaToken'] = self.ua_token
        if self.web_umid_token is not None:
            result['WebUmidToken'] = self.web_umid_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('Merchant') is not None:
            self.merchant = m.get('Merchant')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProduceNode') is not None:
            self.produce_node = m.get('ProduceNode')
        if m.get('BizData') is not None:
            self.biz_data = m.get('BizData')
        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')
        if m.get('CertifyPrincipal') is not None:
            self.certify_principal = m.get('CertifyPrincipal')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('UaToken') is not None:
            self.ua_token = m.get('UaToken')
        if m.get('WebUmidToken') is not None:
            self.web_umid_token = m.get('WebUmidToken')
        return self


class InitDeviceResponseResultObject(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
        protocol: str = None,
        ext_params: str = None,
        ret_code: str = None,
        ret_code_sub: str = None,
        ret_message_sub: str = None,
        message: str = None,
        oss_end_point: str = None,
        access_key_id: str = None,
        access_key_secret: str = None,
        security_token: str = None,
        bucket_name: str = None,
        file_name_prefix: str = None,
        file_name: str = None,
        presigned_url: str = None,
    ):
        self.certify_id = certify_id
        self.protocol = protocol
        self.ext_params = ext_params
        self.ret_code = ret_code
        self.ret_code_sub = ret_code_sub
        self.ret_message_sub = ret_message_sub
        self.message = message
        self.oss_end_point = oss_end_point
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.security_token = security_token
        self.bucket_name = bucket_name
        self.file_name_prefix = file_name_prefix
        self.file_name = file_name
        self.presigned_url = presigned_url

    def validate(self):
        self.validate_required(self.certify_id, 'certify_id')
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.ext_params, 'ext_params')
        self.validate_required(self.ret_code, 'ret_code')
        self.validate_required(self.ret_code_sub, 'ret_code_sub')
        self.validate_required(self.ret_message_sub, 'ret_message_sub')
        self.validate_required(self.message, 'message')
        self.validate_required(self.oss_end_point, 'oss_end_point')
        self.validate_required(self.access_key_id, 'access_key_id')
        self.validate_required(self.access_key_secret, 'access_key_secret')
        self.validate_required(self.security_token, 'security_token')
        self.validate_required(self.bucket_name, 'bucket_name')
        self.validate_required(self.file_name_prefix, 'file_name_prefix')
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.presigned_url, 'presigned_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.ext_params is not None:
            result['ExtParams'] = self.ext_params
        if self.ret_code is not None:
            result['RetCode'] = self.ret_code
        if self.ret_code_sub is not None:
            result['RetCodeSub'] = self.ret_code_sub
        if self.ret_message_sub is not None:
            result['RetMessageSub'] = self.ret_message_sub
        if self.message is not None:
            result['Message'] = self.message
        if self.oss_end_point is not None:
            result['OssEndPoint'] = self.oss_end_point
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.file_name_prefix is not None:
            result['FileNamePrefix'] = self.file_name_prefix
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.presigned_url is not None:
            result['PresignedUrl'] = self.presigned_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('ExtParams') is not None:
            self.ext_params = m.get('ExtParams')
        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')
        if m.get('RetCodeSub') is not None:
            self.ret_code_sub = m.get('RetCodeSub')
        if m.get('RetMessageSub') is not None:
            self.ret_message_sub = m.get('RetMessageSub')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OssEndPoint') is not None:
            self.oss_end_point = m.get('OssEndPoint')
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('FileNamePrefix') is not None:
            self.file_name_prefix = m.get('FileNamePrefix')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('PresignedUrl') is not None:
            self.presigned_url = m.get('PresignedUrl')
        return self


class InitDeviceResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        result_object: InitDeviceResponseResultObject = None,
    ):
        self.request_id = request_id
        self.message = message
        self.code = code
        self.result_object = result_object

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ResultObject') is not None:
            temp_model = InitDeviceResponseResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class InitFaceVerifyRequest(TeaModel):
    def __init__(
        self,
        scene_id: int = None,
        outer_order_no: str = None,
        product_code: str = None,
        cert_type: str = None,
        cert_name: str = None,
        cert_no: str = None,
        return_url: str = None,
        face_contrast_picture: str = None,
        meta_info: str = None,
        mobile: str = None,
        ip: str = None,
        user_id: str = None,
        face_contrast_picture_url: str = None,
        certify_id: str = None,
        oss_bucket_name: str = None,
        oss_object_name: str = None,
        model: str = None,
        callback_url: str = None,
        callback_token: str = None,
        crop: str = None,
    ):
        self.scene_id = scene_id
        self.outer_order_no = outer_order_no
        self.product_code = product_code
        self.cert_type = cert_type
        self.cert_name = cert_name
        self.cert_no = cert_no
        self.return_url = return_url
        self.face_contrast_picture = face_contrast_picture
        self.meta_info = meta_info
        self.mobile = mobile
        self.ip = ip
        self.user_id = user_id
        self.face_contrast_picture_url = face_contrast_picture_url
        self.certify_id = certify_id
        self.oss_bucket_name = oss_bucket_name
        self.oss_object_name = oss_object_name
        self.model = model
        self.callback_url = callback_url
        self.callback_token = callback_token
        self.crop = crop

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.return_url is not None:
            result['ReturnUrl'] = self.return_url
        if self.face_contrast_picture is not None:
            result['FaceContrastPicture'] = self.face_contrast_picture
        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.face_contrast_picture_url is not None:
            result['FaceContrastPictureUrl'] = self.face_contrast_picture_url
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name
        if self.model is not None:
            result['Model'] = self.model
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.callback_token is not None:
            result['CallbackToken'] = self.callback_token
        if self.crop is not None:
            result['Crop'] = self.crop
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('ReturnUrl') is not None:
            self.return_url = m.get('ReturnUrl')
        if m.get('FaceContrastPicture') is not None:
            self.face_contrast_picture = m.get('FaceContrastPicture')
        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('FaceContrastPictureUrl') is not None:
            self.face_contrast_picture_url = m.get('FaceContrastPictureUrl')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('CallbackToken') is not None:
            self.callback_token = m.get('CallbackToken')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        return self


class InitFaceVerifyResponseResultObject(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
        certify_url: str = None,
    ):
        self.certify_id = certify_id
        self.certify_url = certify_url

    def validate(self):
        self.validate_required(self.certify_id, 'certify_id')
        self.validate_required(self.certify_url, 'certify_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.certify_url is not None:
            result['CertifyUrl'] = self.certify_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('CertifyUrl') is not None:
            self.certify_url = m.get('CertifyUrl')
        return self


class InitFaceVerifyResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: InitFaceVerifyResponseResultObject = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result_object = result_object

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = InitFaceVerifyResponseResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class DescribeFaceVerifyRequest(TeaModel):
    def __init__(
        self,
        scene_id: int = None,
        certify_id: str = None,
        picture_return_type: str = None,
    ):
        self.scene_id = scene_id
        self.certify_id = certify_id
        self.picture_return_type = picture_return_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.picture_return_type is not None:
            result['PictureReturnType'] = self.picture_return_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('PictureReturnType') is not None:
            self.picture_return_type = m.get('PictureReturnType')
        return self


class DescribeFaceVerifyResponseResultObject(TeaModel):
    def __init__(
        self,
        sub_code: str = None,
        material_info: str = None,
        identity_info: str = None,
        device_token: str = None,
        passed: str = None,
    ):
        self.sub_code = sub_code
        self.material_info = material_info
        self.identity_info = identity_info
        self.device_token = device_token
        self.passed = passed

    def validate(self):
        self.validate_required(self.sub_code, 'sub_code')
        self.validate_required(self.material_info, 'material_info')
        self.validate_required(self.identity_info, 'identity_info')
        self.validate_required(self.device_token, 'device_token')
        self.validate_required(self.passed, 'passed')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info
        if self.identity_info is not None:
            result['IdentityInfo'] = self.identity_info
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.passed is not None:
            result['Passed'] = self.passed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')
        if m.get('IdentityInfo') is not None:
            self.identity_info = m.get('IdentityInfo')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        return self


class DescribeFaceVerifyResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: DescribeFaceVerifyResponseResultObject = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result_object = result_object

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = DescribeFaceVerifyResponseResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class VerifyDeviceRequest(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
        certify_data: str = None,
        app_version: str = None,
        ext_info: str = None,
        device_token: str = None,
    ):
        self.certify_id = certify_id
        self.certify_data = certify_data
        self.app_version = app_version
        self.ext_info = ext_info
        self.device_token = device_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.certify_data is not None:
            result['CertifyData'] = self.certify_data
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('CertifyData') is not None:
            self.certify_data = m.get('CertifyData')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        return self


class VerifyDeviceResponseResultObject(TeaModel):
    def __init__(
        self,
        validation_ret_code: str = None,
        product_ret_code: str = None,
        ret_code_sub: str = None,
        ret_message_sub: str = None,
        has_next: str = None,
        ext_params: str = None,
    ):
        self.validation_ret_code = validation_ret_code
        self.product_ret_code = product_ret_code
        self.ret_code_sub = ret_code_sub
        self.ret_message_sub = ret_message_sub
        self.has_next = has_next
        self.ext_params = ext_params

    def validate(self):
        self.validate_required(self.validation_ret_code, 'validation_ret_code')
        self.validate_required(self.product_ret_code, 'product_ret_code')
        self.validate_required(self.ret_code_sub, 'ret_code_sub')
        self.validate_required(self.ret_message_sub, 'ret_message_sub')
        self.validate_required(self.has_next, 'has_next')
        self.validate_required(self.ext_params, 'ext_params')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.validation_ret_code is not None:
            result['ValidationRetCode'] = self.validation_ret_code
        if self.product_ret_code is not None:
            result['ProductRetCode'] = self.product_ret_code
        if self.ret_code_sub is not None:
            result['RetCodeSub'] = self.ret_code_sub
        if self.ret_message_sub is not None:
            result['RetMessageSub'] = self.ret_message_sub
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        if self.ext_params is not None:
            result['ExtParams'] = self.ext_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ValidationRetCode') is not None:
            self.validation_ret_code = m.get('ValidationRetCode')
        if m.get('ProductRetCode') is not None:
            self.product_ret_code = m.get('ProductRetCode')
        if m.get('RetCodeSub') is not None:
            self.ret_code_sub = m.get('RetCodeSub')
        if m.get('RetMessageSub') is not None:
            self.ret_message_sub = m.get('RetMessageSub')
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        if m.get('ExtParams') is not None:
            self.ext_params = m.get('ExtParams')
        return self


class VerifyDeviceResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        result_object: VerifyDeviceResponseResultObject = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.result_object = result_object

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            self.result_object.validate()

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
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ResultObject') is not None:
            temp_model = VerifyDeviceResponseResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class ModifyDeviceInfoRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        user_device_id: str = None,
        biz_type: str = None,
        duration: str = None,
        expired_day: str = None,
    ):
        self.device_id = device_id
        self.user_device_id = user_device_id
        self.biz_type = biz_type
        self.duration = duration
        self.expired_day = expired_day

    def validate(self):
        self.validate_required(self.device_id, 'device_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expired_day is not None:
            result['ExpiredDay'] = self.expired_day
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ExpiredDay') is not None:
            self.expired_day = m.get('ExpiredDay')
        return self


class ModifyDeviceInfoResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_id: str = None,
        user_device_id: str = None,
        biz_type: str = None,
        begin_day: str = None,
        expired_day: str = None,
    ):
        self.request_id = request_id
        self.device_id = device_id
        self.user_device_id = user_device_id
        self.biz_type = biz_type
        self.begin_day = begin_day
        self.expired_day = expired_day

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.device_id, 'device_id')
        self.validate_required(self.user_device_id, 'user_device_id')
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.begin_day, 'begin_day')
        self.validate_required(self.expired_day, 'expired_day')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.begin_day is not None:
            result['BeginDay'] = self.begin_day
        if self.expired_day is not None:
            result['ExpiredDay'] = self.expired_day
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BeginDay') is not None:
            self.begin_day = m.get('BeginDay')
        if m.get('ExpiredDay') is not None:
            self.expired_day = m.get('ExpiredDay')
        return self


class DescribeVerifySDKRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        self.validate_required(self.task_id, 'task_id')

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


class DescribeVerifySDKResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sdk_url: str = None,
    ):
        self.request_id = request_id
        self.sdk_url = sdk_url

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.sdk_url, 'sdk_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sdk_url is not None:
            result['SdkUrl'] = self.sdk_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SdkUrl') is not None:
            self.sdk_url = m.get('SdkUrl')
        return self


class DescribeDeviceInfoRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        current_page: int = None,
        device_id: str = None,
        biz_type: str = None,
        user_device_id: str = None,
        expired_start_day: str = None,
        expired_end_day: str = None,
    ):
        self.page_size = page_size
        self.current_page = current_page
        self.device_id = device_id
        self.biz_type = biz_type
        self.user_device_id = user_device_id
        self.expired_start_day = expired_start_day
        self.expired_end_day = expired_end_day

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        if self.expired_start_day is not None:
            result['ExpiredStartDay'] = self.expired_start_day
        if self.expired_end_day is not None:
            result['ExpiredEndDay'] = self.expired_end_day
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
        if m.get('ExpiredStartDay') is not None:
            self.expired_start_day = m.get('ExpiredStartDay')
        if m.get('ExpiredEndDay') is not None:
            self.expired_end_day = m.get('ExpiredEndDay')
        return self


class DescribeDeviceInfoResponseDeviceInfoListDeviceInfo(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        user_device_id: str = None,
        biz_type: str = None,
        begin_day: str = None,
        expired_day: str = None,
    ):
        self.device_id = device_id
        self.user_device_id = user_device_id
        self.biz_type = biz_type
        self.begin_day = begin_day
        self.expired_day = expired_day

    def validate(self):
        self.validate_required(self.device_id, 'device_id')
        self.validate_required(self.user_device_id, 'user_device_id')
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.begin_day, 'begin_day')
        self.validate_required(self.expired_day, 'expired_day')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.begin_day is not None:
            result['BeginDay'] = self.begin_day
        if self.expired_day is not None:
            result['ExpiredDay'] = self.expired_day
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BeginDay') is not None:
            self.begin_day = m.get('BeginDay')
        if m.get('ExpiredDay') is not None:
            self.expired_day = m.get('ExpiredDay')
        return self


class DescribeDeviceInfoResponseDeviceInfoList(TeaModel):
    def __init__(
        self,
        device_info: List[DescribeDeviceInfoResponseDeviceInfoListDeviceInfo] = None,
    ):
        self.device_info = device_info

    def validate(self):
        self.validate_required(self.device_info, 'device_info')
        if self.device_info:
            for k in self.device_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeviceInfo'] = []
        if self.device_info is not None:
            for k in self.device_info:
                result['DeviceInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.device_info = []
        if m.get('DeviceInfo') is not None:
            for k in m.get('DeviceInfo'):
                temp_model = DescribeDeviceInfoResponseDeviceInfoListDeviceInfo()
                self.device_info.append(temp_model.from_map(k))
        return self


class DescribeDeviceInfoResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_size: int = None,
        current_page: int = None,
        total_count: int = None,
        device_info_list: DescribeDeviceInfoResponseDeviceInfoList = None,
    ):
        self.request_id = request_id
        self.page_size = page_size
        self.current_page = current_page
        self.total_count = total_count
        self.device_info_list = device_info_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.current_page, 'current_page')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.device_info_list, 'device_info_list')
        if self.device_info_list:
            self.device_info_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.device_info_list is not None:
            result['DeviceInfoList'] = self.device_info_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('DeviceInfoList') is not None:
            temp_model = DescribeDeviceInfoResponseDeviceInfoList()
            self.device_info_list = temp_model.from_map(m['DeviceInfoList'])
        return self


class CreateVerifySDKRequest(TeaModel):
    def __init__(
        self,
        app_url: str = None,
        platform: str = None,
    ):
        self.app_url = app_url
        self.platform = platform

    def validate(self):
        self.validate_required(self.app_url, 'app_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_url is not None:
            result['AppUrl'] = self.app_url
        if self.platform is not None:
            result['Platform'] = self.platform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUrl') is not None:
            self.app_url = m.get('AppUrl')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        return self


class CreateVerifySDKResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateAuthKeyRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        user_device_id: str = None,
        test: bool = None,
        auth_years: int = None,
    ):
        self.biz_type = biz_type
        self.user_device_id = user_device_id
        self.test = test
        self.auth_years = auth_years

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        if self.test is not None:
            result['Test'] = self.test
        if self.auth_years is not None:
            result['AuthYears'] = self.auth_years
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
        if m.get('Test') is not None:
            self.test = m.get('Test')
        if m.get('AuthYears') is not None:
            self.auth_years = m.get('AuthYears')
        return self


class CreateAuthKeyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        auth_key: str = None,
    ):
        self.request_id = request_id
        self.auth_key = auth_key

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.auth_key, 'auth_key')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        return self


class DetectFaceAttributesRequest(TeaModel):
    def __init__(
        self,
        material_value: str = None,
        biz_type: str = None,
    ):
        self.material_value = material_value
        self.biz_type = biz_type

    def validate(self):
        self.validate_required(self.material_value, 'material_value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.material_value is not None:
            result['MaterialValue'] = self.material_value
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaterialValue') is not None:
            self.material_value = m.get('MaterialValue')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfoFaceRect(TeaModel):
    def __init__(
        self,
        top: int = None,
        left: int = None,
        width: int = None,
        height: int = None,
    ):
        self.top = top
        self.left = left
        self.width = width
        self.height = height

    def validate(self):
        self.validate_required(self.top, 'top')
        self.validate_required(self.left, 'left')
        self.validate_required(self.width, 'width')
        self.validate_required(self.height, 'height')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.top is not None:
            result['Top'] = self.top
        if self.left is not None:
            result['Left'] = self.left
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfoFaceAttributesSmiling(TeaModel):
    def __init__(
        self,
        value: float = None,
        threshold: float = None,
    ):
        self.value = value
        self.threshold = threshold

    def validate(self):
        self.validate_required(self.value, 'value')
        self.validate_required(self.threshold, 'threshold')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfoFaceAttributesHeadpose(TeaModel):
    def __init__(
        self,
        pitch_angle: float = None,
        roll_angle: float = None,
        yaw_angle: float = None,
    ):
        self.pitch_angle = pitch_angle
        self.roll_angle = roll_angle
        self.yaw_angle = yaw_angle

    def validate(self):
        self.validate_required(self.pitch_angle, 'pitch_angle')
        self.validate_required(self.roll_angle, 'roll_angle')
        self.validate_required(self.yaw_angle, 'yaw_angle')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pitch_angle is not None:
            result['PitchAngle'] = self.pitch_angle
        if self.roll_angle is not None:
            result['RollAngle'] = self.roll_angle
        if self.yaw_angle is not None:
            result['YawAngle'] = self.yaw_angle
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PitchAngle') is not None:
            self.pitch_angle = m.get('PitchAngle')
        if m.get('RollAngle') is not None:
            self.roll_angle = m.get('RollAngle')
        if m.get('YawAngle') is not None:
            self.yaw_angle = m.get('YawAngle')
        return self


class DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfoFaceAttributes(TeaModel):
    def __init__(
        self,
        glasses: str = None,
        facetype: str = None,
        blur: float = None,
        facequal: float = None,
        integrity: int = None,
        respirator: str = None,
        smiling: DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfoFaceAttributesSmiling = None,
        headpose: DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfoFaceAttributesHeadpose = None,
    ):
        self.glasses = glasses
        self.facetype = facetype
        self.blur = blur
        self.facequal = facequal
        self.integrity = integrity
        self.respirator = respirator
        self.smiling = smiling
        self.headpose = headpose

    def validate(self):
        self.validate_required(self.glasses, 'glasses')
        self.validate_required(self.facetype, 'facetype')
        self.validate_required(self.blur, 'blur')
        self.validate_required(self.facequal, 'facequal')
        self.validate_required(self.integrity, 'integrity')
        self.validate_required(self.respirator, 'respirator')
        self.validate_required(self.smiling, 'smiling')
        if self.smiling:
            self.smiling.validate()
        self.validate_required(self.headpose, 'headpose')
        if self.headpose:
            self.headpose.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.glasses is not None:
            result['Glasses'] = self.glasses
        if self.facetype is not None:
            result['Facetype'] = self.facetype
        if self.blur is not None:
            result['Blur'] = self.blur
        if self.facequal is not None:
            result['Facequal'] = self.facequal
        if self.integrity is not None:
            result['Integrity'] = self.integrity
        if self.respirator is not None:
            result['Respirator'] = self.respirator
        if self.smiling is not None:
            result['Smiling'] = self.smiling.to_map()
        if self.headpose is not None:
            result['Headpose'] = self.headpose.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Glasses') is not None:
            self.glasses = m.get('Glasses')
        if m.get('Facetype') is not None:
            self.facetype = m.get('Facetype')
        if m.get('Blur') is not None:
            self.blur = m.get('Blur')
        if m.get('Facequal') is not None:
            self.facequal = m.get('Facequal')
        if m.get('Integrity') is not None:
            self.integrity = m.get('Integrity')
        if m.get('Respirator') is not None:
            self.respirator = m.get('Respirator')
        if m.get('Smiling') is not None:
            temp_model = DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfoFaceAttributesSmiling()
            self.smiling = temp_model.from_map(m['Smiling'])
        if m.get('Headpose') is not None:
            temp_model = DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfoFaceAttributesHeadpose()
            self.headpose = temp_model.from_map(m['Headpose'])
        return self


class DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfo(TeaModel):
    def __init__(
        self,
        face_rect: DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfoFaceRect = None,
        face_attributes: DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfoFaceAttributes = None,
    ):
        self.face_rect = face_rect
        self.face_attributes = face_attributes

    def validate(self):
        self.validate_required(self.face_rect, 'face_rect')
        if self.face_rect:
            self.face_rect.validate()
        self.validate_required(self.face_attributes, 'face_attributes')
        if self.face_attributes:
            self.face_attributes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_rect is not None:
            result['FaceRect'] = self.face_rect.to_map()
        if self.face_attributes is not None:
            result['FaceAttributes'] = self.face_attributes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceRect') is not None:
            temp_model = DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfoFaceRect()
            self.face_rect = temp_model.from_map(m['FaceRect'])
        if m.get('FaceAttributes') is not None:
            temp_model = DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfoFaceAttributes()
            self.face_attributes = temp_model.from_map(m['FaceAttributes'])
        return self


class DetectFaceAttributesResponseDataFaceInfos(TeaModel):
    def __init__(
        self,
        face_attributes_detect_info: List[DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfo] = None,
    ):
        self.face_attributes_detect_info = face_attributes_detect_info

    def validate(self):
        self.validate_required(self.face_attributes_detect_info, 'face_attributes_detect_info')
        if self.face_attributes_detect_info:
            for k in self.face_attributes_detect_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FaceAttributesDetectInfo'] = []
        if self.face_attributes_detect_info is not None:
            for k in self.face_attributes_detect_info:
                result['FaceAttributesDetectInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.face_attributes_detect_info = []
        if m.get('FaceAttributesDetectInfo') is not None:
            for k in m.get('FaceAttributesDetectInfo'):
                temp_model = DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfo()
                self.face_attributes_detect_info.append(temp_model.from_map(k))
        return self


class DetectFaceAttributesResponseData(TeaModel):
    def __init__(
        self,
        img_width: int = None,
        img_height: int = None,
        face_infos: DetectFaceAttributesResponseDataFaceInfos = None,
    ):
        self.img_width = img_width
        self.img_height = img_height
        self.face_infos = face_infos

    def validate(self):
        self.validate_required(self.img_width, 'img_width')
        self.validate_required(self.img_height, 'img_height')
        self.validate_required(self.face_infos, 'face_infos')
        if self.face_infos:
            self.face_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.img_width is not None:
            result['ImgWidth'] = self.img_width
        if self.img_height is not None:
            result['ImgHeight'] = self.img_height
        if self.face_infos is not None:
            result['FaceInfos'] = self.face_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImgWidth') is not None:
            self.img_width = m.get('ImgWidth')
        if m.get('ImgHeight') is not None:
            self.img_height = m.get('ImgHeight')
        if m.get('FaceInfos') is not None:
            temp_model = DetectFaceAttributesResponseDataFaceInfos()
            self.face_infos = temp_model.from_map(m['FaceInfos'])
        return self


class DetectFaceAttributesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: DetectFaceAttributesResponseData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

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
            result['Data'] = self.data.to_map()
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
            temp_model = DetectFaceAttributesResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class CompareFacesRequest(TeaModel):
    def __init__(
        self,
        target_image_type: str = None,
        source_image_type: str = None,
        source_image_value: str = None,
        target_image_value: str = None,
    ):
        self.target_image_type = target_image_type
        self.source_image_type = source_image_type
        self.source_image_value = source_image_value
        self.target_image_value = target_image_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_image_type is not None:
            result['TargetImageType'] = self.target_image_type
        if self.source_image_type is not None:
            result['SourceImageType'] = self.source_image_type
        if self.source_image_value is not None:
            result['SourceImageValue'] = self.source_image_value
        if self.target_image_value is not None:
            result['TargetImageValue'] = self.target_image_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetImageType') is not None:
            self.target_image_type = m.get('TargetImageType')
        if m.get('SourceImageType') is not None:
            self.source_image_type = m.get('SourceImageType')
        if m.get('SourceImageValue') is not None:
            self.source_image_value = m.get('SourceImageValue')
        if m.get('TargetImageValue') is not None:
            self.target_image_value = m.get('TargetImageValue')
        return self


class CompareFacesResponseData(TeaModel):
    def __init__(
        self,
        similarity_score: float = None,
        confidence_thresholds: str = None,
    ):
        self.similarity_score = similarity_score
        self.confidence_thresholds = confidence_thresholds

    def validate(self):
        self.validate_required(self.similarity_score, 'similarity_score')
        self.validate_required(self.confidence_thresholds, 'confidence_thresholds')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.similarity_score is not None:
            result['SimilarityScore'] = self.similarity_score
        if self.confidence_thresholds is not None:
            result['ConfidenceThresholds'] = self.confidence_thresholds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SimilarityScore') is not None:
            self.similarity_score = m.get('SimilarityScore')
        if m.get('ConfidenceThresholds') is not None:
            self.confidence_thresholds = m.get('ConfidenceThresholds')
        return self


class CompareFacesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: CompareFacesResponseData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

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
            result['Data'] = self.data.to_map()
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
            temp_model = CompareFacesResponseData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeFaceUsageRequest(TeaModel):
    def __init__(
        self,
        start_date: str = None,
        end_date: str = None,
    ):
        self.start_date = start_date
        self.end_date = end_date

    def validate(self):
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class DescribeFaceUsageResponseFaceUsageList(TeaModel):
    def __init__(
        self,
        date: str = None,
        total_count: int = None,
    ):
        self.date = date
        self.total_count = total_count

    def validate(self):
        self.validate_required(self.date, 'date')
        self.validate_required(self.total_count, 'total_count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeFaceUsageResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        face_usage_list: List[DescribeFaceUsageResponseFaceUsageList] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.face_usage_list = face_usage_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.face_usage_list, 'face_usage_list')
        if self.face_usage_list:
            for k in self.face_usage_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['FaceUsageList'] = []
        if self.face_usage_list is not None:
            for k in self.face_usage_list:
                result['FaceUsageList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.face_usage_list = []
        if m.get('FaceUsageList') is not None:
            for k in m.get('FaceUsageList'):
                temp_model = DescribeFaceUsageResponseFaceUsageList()
                self.face_usage_list.append(temp_model.from_map(k))
        return self


class DescribeVerifyRecordsRequest(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        current_page: int = None,
        biz_type: str = None,
        start_date: str = None,
        end_date: str = None,
        biz_id: str = None,
        id_card_num: str = None,
        status_list: str = None,
        query_id: str = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.current_page = current_page
        self.biz_type = biz_type
        self.start_date = start_date
        self.end_date = end_date
        self.biz_id = biz_id
        self.id_card_num = id_card_num
        self.status_list = status_list
        self.query_id = query_id

    def validate(self):
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.current_page, 'current_page')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.id_card_num is not None:
            result['IdCardNum'] = self.id_card_num
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('IdCardNum') is not None:
            self.id_card_num = m.get('IdCardNum')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        return self


class DescribeVerifyRecordsResponseRecordsListMaterialIdCardInfo(TeaModel):
    def __init__(
        self,
        front_image_url: str = None,
        back_image_url: str = None,
        name: str = None,
        number: str = None,
        address: str = None,
        birth: str = None,
        sex: str = None,
        nationality: str = None,
        authority: str = None,
        start_date: str = None,
        end_date: str = None,
    ):
        self.front_image_url = front_image_url
        self.back_image_url = back_image_url
        self.name = name
        self.number = number
        self.address = address
        self.birth = birth
        self.sex = sex
        self.nationality = nationality
        self.authority = authority
        self.start_date = start_date
        self.end_date = end_date

    def validate(self):
        self.validate_required(self.front_image_url, 'front_image_url')
        self.validate_required(self.back_image_url, 'back_image_url')
        self.validate_required(self.name, 'name')
        self.validate_required(self.number, 'number')
        self.validate_required(self.address, 'address')
        self.validate_required(self.birth, 'birth')
        self.validate_required(self.sex, 'sex')
        self.validate_required(self.nationality, 'nationality')
        self.validate_required(self.authority, 'authority')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.front_image_url is not None:
            result['FrontImageUrl'] = self.front_image_url
        if self.back_image_url is not None:
            result['BackImageUrl'] = self.back_image_url
        if self.name is not None:
            result['Name'] = self.name
        if self.number is not None:
            result['Number'] = self.number
        if self.address is not None:
            result['Address'] = self.address
        if self.birth is not None:
            result['Birth'] = self.birth
        if self.sex is not None:
            result['Sex'] = self.sex
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        if self.authority is not None:
            result['Authority'] = self.authority
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrontImageUrl') is not None:
            self.front_image_url = m.get('FrontImageUrl')
        if m.get('BackImageUrl') is not None:
            self.back_image_url = m.get('BackImageUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Birth') is not None:
            self.birth = m.get('Birth')
        if m.get('Sex') is not None:
            self.sex = m.get('Sex')
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
        if m.get('Authority') is not None:
            self.authority = m.get('Authority')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class DescribeVerifyRecordsResponseRecordsListMaterial(TeaModel):
    def __init__(
        self,
        face_image_url: str = None,
        id_card_name: str = None,
        id_card_number: str = None,
        id_card_info: DescribeVerifyRecordsResponseRecordsListMaterialIdCardInfo = None,
    ):
        self.face_image_url = face_image_url
        self.id_card_name = id_card_name
        self.id_card_number = id_card_number
        self.id_card_info = id_card_info

    def validate(self):
        self.validate_required(self.face_image_url, 'face_image_url')
        self.validate_required(self.id_card_name, 'id_card_name')
        self.validate_required(self.id_card_number, 'id_card_number')
        self.validate_required(self.id_card_info, 'id_card_info')
        if self.id_card_info:
            self.id_card_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_info is not None:
            result['IdCardInfo'] = self.id_card_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardInfo') is not None:
            temp_model = DescribeVerifyRecordsResponseRecordsListMaterialIdCardInfo()
            self.id_card_info = temp_model.from_map(m['IdCardInfo'])
        return self


class DescribeVerifyRecordsResponseRecordsList(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        biz_id: str = None,
        data_stats: str = None,
        verify_id: str = None,
        finish_time: int = None,
        status: int = None,
        id_card_face_comparison_score: float = None,
        authority_comparison_score: float = None,
        material: DescribeVerifyRecordsResponseRecordsListMaterial = None,
    ):
        self.biz_type = biz_type
        self.biz_id = biz_id
        self.data_stats = data_stats
        self.verify_id = verify_id
        self.finish_time = finish_time
        self.status = status
        self.id_card_face_comparison_score = id_card_face_comparison_score
        self.authority_comparison_score = authority_comparison_score
        self.material = material

    def validate(self):
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.biz_id, 'biz_id')
        self.validate_required(self.data_stats, 'data_stats')
        self.validate_required(self.verify_id, 'verify_id')
        self.validate_required(self.finish_time, 'finish_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.id_card_face_comparison_score, 'id_card_face_comparison_score')
        self.validate_required(self.authority_comparison_score, 'authority_comparison_score')
        self.validate_required(self.material, 'material')
        if self.material:
            self.material.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.data_stats is not None:
            result['DataStats'] = self.data_stats
        if self.verify_id is not None:
            result['VerifyId'] = self.verify_id
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.status is not None:
            result['Status'] = self.status
        if self.id_card_face_comparison_score is not None:
            result['IdCardFaceComparisonScore'] = self.id_card_face_comparison_score
        if self.authority_comparison_score is not None:
            result['AuthorityComparisonScore'] = self.authority_comparison_score
        if self.material is not None:
            result['Material'] = self.material.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('DataStats') is not None:
            self.data_stats = m.get('DataStats')
        if m.get('VerifyId') is not None:
            self.verify_id = m.get('VerifyId')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('IdCardFaceComparisonScore') is not None:
            self.id_card_face_comparison_score = m.get('IdCardFaceComparisonScore')
        if m.get('AuthorityComparisonScore') is not None:
            self.authority_comparison_score = m.get('AuthorityComparisonScore')
        if m.get('Material') is not None:
            temp_model = DescribeVerifyRecordsResponseRecordsListMaterial()
            self.material = temp_model.from_map(m['Material'])
        return self


class DescribeVerifyRecordsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        page_size: int = None,
        current_page: int = None,
        query_id: str = None,
        records_list: List[DescribeVerifyRecordsResponseRecordsList] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.page_size = page_size
        self.current_page = current_page
        self.query_id = query_id
        self.records_list = records_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.current_page, 'current_page')
        self.validate_required(self.query_id, 'query_id')
        self.validate_required(self.records_list, 'records_list')
        if self.records_list:
            for k in self.records_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        result['RecordsList'] = []
        if self.records_list is not None:
            for k in self.records_list:
                result['RecordsList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        self.records_list = []
        if m.get('RecordsList') is not None:
            for k in m.get('RecordsList'):
                temp_model = DescribeVerifyRecordsResponseRecordsList()
                self.records_list.append(temp_model.from_map(k))
        return self


class UpdateVerifySettingRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        biz_name: str = None,
        solution: str = None,
        guide_step: bool = None,
        privacy_step: bool = None,
        result_step: bool = None,
    ):
        self.biz_type = biz_type
        self.biz_name = biz_name
        self.solution = solution
        self.guide_step = guide_step
        self.privacy_step = privacy_step
        self.result_step = result_step

    def validate(self):
        self.validate_required(self.biz_type, 'biz_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.solution is not None:
            result['Solution'] = self.solution
        if self.guide_step is not None:
            result['GuideStep'] = self.guide_step
        if self.privacy_step is not None:
            result['PrivacyStep'] = self.privacy_step
        if self.result_step is not None:
            result['ResultStep'] = self.result_step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        if m.get('GuideStep') is not None:
            self.guide_step = m.get('GuideStep')
        if m.get('PrivacyStep') is not None:
            self.privacy_step = m.get('PrivacyStep')
        if m.get('ResultStep') is not None:
            self.result_step = m.get('ResultStep')
        return self


class UpdateVerifySettingResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        biz_type: str = None,
        biz_name: str = None,
        solution: str = None,
        step_list: List[str] = None,
    ):
        self.request_id = request_id
        self.biz_type = biz_type
        self.biz_name = biz_name
        self.solution = solution
        self.step_list = step_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.biz_name, 'biz_name')
        self.validate_required(self.solution, 'solution')
        self.validate_required(self.step_list, 'step_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.solution is not None:
            result['Solution'] = self.solution
        if self.step_list is not None:
            result['StepList'] = self.step_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        if m.get('StepList') is not None:
            self.step_list = m.get('StepList')
        return self


class CreateVerifySettingRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        biz_name: str = None,
        solution: str = None,
        guide_step: bool = None,
        privacy_step: bool = None,
        result_step: bool = None,
    ):
        self.biz_type = biz_type
        self.biz_name = biz_name
        self.solution = solution
        self.guide_step = guide_step
        self.privacy_step = privacy_step
        self.result_step = result_step

    def validate(self):
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.biz_name, 'biz_name')
        self.validate_required(self.solution, 'solution')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.solution is not None:
            result['Solution'] = self.solution
        if self.guide_step is not None:
            result['GuideStep'] = self.guide_step
        if self.privacy_step is not None:
            result['PrivacyStep'] = self.privacy_step
        if self.result_step is not None:
            result['ResultStep'] = self.result_step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        if m.get('GuideStep') is not None:
            self.guide_step = m.get('GuideStep')
        if m.get('PrivacyStep') is not None:
            self.privacy_step = m.get('PrivacyStep')
        if m.get('ResultStep') is not None:
            self.result_step = m.get('ResultStep')
        return self


class CreateVerifySettingResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        biz_type: str = None,
        biz_name: str = None,
        solution: str = None,
        step_list: List[str] = None,
    ):
        self.request_id = request_id
        self.biz_type = biz_type
        self.biz_name = biz_name
        self.solution = solution
        self.step_list = step_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.biz_name, 'biz_name')
        self.validate_required(self.solution, 'solution')
        self.validate_required(self.step_list, 'step_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.solution is not None:
            result['Solution'] = self.solution
        if self.step_list is not None:
            result['StepList'] = self.step_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        if m.get('StepList') is not None:
            self.step_list = m.get('StepList')
        return self


class DescribeVerifySettingRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DescribeVerifySettingResponseVerifySettingList(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        biz_name: str = None,
        solution: str = None,
        step_list: List[str] = None,
    ):
        self.biz_type = biz_type
        self.biz_name = biz_name
        self.solution = solution
        self.step_list = step_list

    def validate(self):
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.biz_name, 'biz_name')
        self.validate_required(self.solution, 'solution')
        self.validate_required(self.step_list, 'step_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.solution is not None:
            result['Solution'] = self.solution
        if self.step_list is not None:
            result['StepList'] = self.step_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        if m.get('StepList') is not None:
            self.step_list = m.get('StepList')
        return self


class DescribeVerifySettingResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        verify_setting_list: List[DescribeVerifySettingResponseVerifySettingList] = None,
    ):
        self.request_id = request_id
        self.verify_setting_list = verify_setting_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.verify_setting_list, 'verify_setting_list')
        if self.verify_setting_list:
            for k in self.verify_setting_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['VerifySettingList'] = []
        if self.verify_setting_list is not None:
            for k in self.verify_setting_list:
                result['VerifySettingList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.verify_setting_list = []
        if m.get('VerifySettingList') is not None:
            for k in m.get('VerifySettingList'):
                temp_model = DescribeVerifySettingResponseVerifySettingList()
                self.verify_setting_list.append(temp_model.from_map(k))
        return self


class DescribeVerifyUsageRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        start_date: str = None,
        end_date: str = None,
    ):
        self.biz_type = biz_type
        self.start_date = start_date
        self.end_date = end_date

    def validate(self):
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class DescribeVerifyUsageResponseVerifyUsageList(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        date: str = None,
        total_count: int = None,
        pass_count: int = None,
        fail_count: int = None,
    ):
        self.biz_type = biz_type
        self.date = date
        self.total_count = total_count
        self.pass_count = pass_count
        self.fail_count = fail_count

    def validate(self):
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.date, 'date')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.pass_count, 'pass_count')
        self.validate_required(self.fail_count, 'fail_count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.date is not None:
            result['Date'] = self.date
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.pass_count is not None:
            result['PassCount'] = self.pass_count
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PassCount') is not None:
            self.pass_count = m.get('PassCount')
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        return self


class DescribeVerifyUsageResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        verify_usage_list: List[DescribeVerifyUsageResponseVerifyUsageList] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.verify_usage_list = verify_usage_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.verify_usage_list, 'verify_usage_list')
        if self.verify_usage_list:
            for k in self.verify_usage_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['VerifyUsageList'] = []
        if self.verify_usage_list is not None:
            for k in self.verify_usage_list:
                result['VerifyUsageList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.verify_usage_list = []
        if m.get('VerifyUsageList') is not None:
            for k in m.get('VerifyUsageList'):
                temp_model = DescribeVerifyUsageResponseVerifyUsageList()
                self.verify_usage_list.append(temp_model.from_map(k))
        return self


class DescribeUserStatusRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DescribeUserStatusResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        enabled: bool = None,
    ):
        self.request_id = request_id
        self.enabled = enabled

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.enabled, 'enabled')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class DescribeUploadInfoRequest(TeaModel):
    def __init__(
        self,
        biz: str = None,
    ):
        self.biz = biz

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz is not None:
            result['Biz'] = self.biz
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Biz') is not None:
            self.biz = m.get('Biz')
        return self


class DescribeUploadInfoResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        accessid: str = None,
        policy: str = None,
        signature: str = None,
        folder: str = None,
        host: str = None,
        expire: int = None,
    ):
        self.request_id = request_id
        self.accessid = accessid
        self.policy = policy
        self.signature = signature
        self.folder = folder
        self.host = host
        self.expire = expire

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.accessid, 'accessid')
        self.validate_required(self.policy, 'policy')
        self.validate_required(self.signature, 'signature')
        self.validate_required(self.folder, 'folder')
        self.validate_required(self.host, 'host')
        self.validate_required(self.expire, 'expire')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.accessid is not None:
            result['Accessid'] = self.accessid
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.folder is not None:
            result['Folder'] = self.folder
        if self.host is not None:
            result['Host'] = self.host
        if self.expire is not None:
            result['Expire'] = self.expire
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Accessid') is not None:
            self.accessid = m.get('Accessid')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('Folder') is not None:
            self.folder = m.get('Folder')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        return self


class DescribeRPSDKRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        task_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.task_id = task_id

    def validate(self):
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeRPSDKResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sdk_url: str = None,
    ):
        self.request_id = request_id
        self.sdk_url = sdk_url

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.sdk_url, 'sdk_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sdk_url is not None:
            result['SdkUrl'] = self.sdk_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SdkUrl') is not None:
            self.sdk_url = m.get('SdkUrl')
        return self


class CreateRPSDKRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        app_url: str = None,
        platform: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.app_url = app_url
        self.platform = platform

    def validate(self):
        self.validate_required(self.app_url, 'app_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.app_url is not None:
            result['AppUrl'] = self.app_url
        if self.platform is not None:
            result['Platform'] = self.platform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AppUrl') is not None:
            self.app_url = m.get('AppUrl')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        return self


class CreateRPSDKResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class VerifyMaterialRequest(TeaModel):
    def __init__(
        self,
        id_card_back_image_url: str = None,
        face_image_url: str = None,
        biz_type: str = None,
        biz_id: str = None,
        name: str = None,
        id_card_number: str = None,
        id_card_front_image_url: str = None,
        user_id: str = None,
    ):
        self.id_card_back_image_url = id_card_back_image_url
        self.face_image_url = face_image_url
        self.biz_type = biz_type
        self.biz_id = biz_id
        self.name = name
        self.id_card_number = id_card_number
        self.id_card_front_image_url = id_card_front_image_url
        self.user_id = user_id

    def validate(self):
        self.validate_required(self.face_image_url, 'face_image_url')
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.biz_id, 'biz_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.id_card_number, 'id_card_number')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id_card_back_image_url is not None:
            result['IdCardBackImageUrl'] = self.id_card_back_image_url
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.name is not None:
            result['Name'] = self.name
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_front_image_url is not None:
            result['IdCardFrontImageUrl'] = self.id_card_front_image_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdCardBackImageUrl') is not None:
            self.id_card_back_image_url = m.get('IdCardBackImageUrl')
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardFrontImageUrl') is not None:
            self.id_card_front_image_url = m.get('IdCardFrontImageUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class VerifyMaterialResponseMaterialIdCardInfo(TeaModel):
    def __init__(
        self,
        number: str = None,
        address: str = None,
        nationality: str = None,
        end_date: str = None,
        front_image_url: str = None,
        authority: str = None,
        name: str = None,
        birth: str = None,
        back_image_url: str = None,
        start_date: str = None,
    ):
        self.number = number
        self.address = address
        self.nationality = nationality
        self.end_date = end_date
        self.front_image_url = front_image_url
        self.authority = authority
        self.name = name
        self.birth = birth
        self.back_image_url = back_image_url
        self.start_date = start_date

    def validate(self):
        self.validate_required(self.number, 'number')
        self.validate_required(self.address, 'address')
        self.validate_required(self.nationality, 'nationality')
        self.validate_required(self.end_date, 'end_date')
        self.validate_required(self.front_image_url, 'front_image_url')
        self.validate_required(self.authority, 'authority')
        self.validate_required(self.name, 'name')
        self.validate_required(self.birth, 'birth')
        self.validate_required(self.back_image_url, 'back_image_url')
        self.validate_required(self.start_date, 'start_date')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number is not None:
            result['Number'] = self.number
        if self.address is not None:
            result['Address'] = self.address
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.front_image_url is not None:
            result['FrontImageUrl'] = self.front_image_url
        if self.authority is not None:
            result['Authority'] = self.authority
        if self.name is not None:
            result['Name'] = self.name
        if self.birth is not None:
            result['Birth'] = self.birth
        if self.back_image_url is not None:
            result['BackImageUrl'] = self.back_image_url
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('FrontImageUrl') is not None:
            self.front_image_url = m.get('FrontImageUrl')
        if m.get('Authority') is not None:
            self.authority = m.get('Authority')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Birth') is not None:
            self.birth = m.get('Birth')
        if m.get('BackImageUrl') is not None:
            self.back_image_url = m.get('BackImageUrl')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class VerifyMaterialResponseMaterial(TeaModel):
    def __init__(
        self,
        face_image_url: str = None,
        id_card_name: str = None,
        id_card_number: str = None,
        face_quality: str = None,
        face_global_url: str = None,
        face_mask: str = None,
        id_card_info: VerifyMaterialResponseMaterialIdCardInfo = None,
    ):
        self.face_image_url = face_image_url
        self.id_card_name = id_card_name
        self.id_card_number = id_card_number
        self.face_quality = face_quality
        self.face_global_url = face_global_url
        self.face_mask = face_mask
        self.id_card_info = id_card_info

    def validate(self):
        self.validate_required(self.face_image_url, 'face_image_url')
        self.validate_required(self.id_card_name, 'id_card_name')
        self.validate_required(self.id_card_number, 'id_card_number')
        self.validate_required(self.face_quality, 'face_quality')
        self.validate_required(self.face_global_url, 'face_global_url')
        self.validate_required(self.face_mask, 'face_mask')
        self.validate_required(self.id_card_info, 'id_card_info')
        if self.id_card_info:
            self.id_card_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        if self.face_global_url is not None:
            result['FaceGlobalUrl'] = self.face_global_url
        if self.face_mask is not None:
            result['FaceMask'] = self.face_mask
        if self.id_card_info is not None:
            result['IdCardInfo'] = self.id_card_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        if m.get('FaceGlobalUrl') is not None:
            self.face_global_url = m.get('FaceGlobalUrl')
        if m.get('FaceMask') is not None:
            self.face_mask = m.get('FaceMask')
        if m.get('IdCardInfo') is not None:
            temp_model = VerifyMaterialResponseMaterialIdCardInfo()
            self.id_card_info = temp_model.from_map(m['IdCardInfo'])
        return self


class VerifyMaterialResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        verify_token: str = None,
        verify_status: int = None,
        authority_comparision_score: float = None,
        id_card_face_comparison_score: float = None,
        material: VerifyMaterialResponseMaterial = None,
    ):
        self.request_id = request_id
        self.verify_token = verify_token
        self.verify_status = verify_status
        self.authority_comparision_score = authority_comparision_score
        self.id_card_face_comparison_score = id_card_face_comparison_score
        self.material = material

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.verify_token, 'verify_token')
        self.validate_required(self.verify_status, 'verify_status')
        self.validate_required(self.authority_comparision_score, 'authority_comparision_score')
        self.validate_required(self.id_card_face_comparison_score, 'id_card_face_comparison_score')
        self.validate_required(self.material, 'material')
        if self.material:
            self.material.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.verify_token is not None:
            result['VerifyToken'] = self.verify_token
        if self.verify_status is not None:
            result['VerifyStatus'] = self.verify_status
        if self.authority_comparision_score is not None:
            result['AuthorityComparisionScore'] = self.authority_comparision_score
        if self.id_card_face_comparison_score is not None:
            result['IdCardFaceComparisonScore'] = self.id_card_face_comparison_score
        if self.material is not None:
            result['Material'] = self.material.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VerifyToken') is not None:
            self.verify_token = m.get('VerifyToken')
        if m.get('VerifyStatus') is not None:
            self.verify_status = m.get('VerifyStatus')
        if m.get('AuthorityComparisionScore') is not None:
            self.authority_comparision_score = m.get('AuthorityComparisionScore')
        if m.get('IdCardFaceComparisonScore') is not None:
            self.id_card_face_comparison_score = m.get('IdCardFaceComparisonScore')
        if m.get('Material') is not None:
            temp_model = VerifyMaterialResponseMaterial()
            self.material = temp_model.from_map(m['Material'])
        return self


class DescribeVerifyResultRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
    ):
        self.biz_id = biz_id
        self.biz_type = biz_type

    def validate(self):
        self.validate_required(self.biz_id, 'biz_id')
        self.validate_required(self.biz_type, 'biz_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class DescribeVerifyResultResponseMaterialIdCardInfo(TeaModel):
    def __init__(
        self,
        number: str = None,
        address: str = None,
        nationality: str = None,
        end_date: str = None,
        front_image_url: str = None,
        authority: str = None,
        name: str = None,
        birth: str = None,
        back_image_url: str = None,
        start_date: str = None,
    ):
        self.number = number
        self.address = address
        self.nationality = nationality
        self.end_date = end_date
        self.front_image_url = front_image_url
        self.authority = authority
        self.name = name
        self.birth = birth
        self.back_image_url = back_image_url
        self.start_date = start_date

    def validate(self):
        self.validate_required(self.number, 'number')
        self.validate_required(self.address, 'address')
        self.validate_required(self.nationality, 'nationality')
        self.validate_required(self.end_date, 'end_date')
        self.validate_required(self.front_image_url, 'front_image_url')
        self.validate_required(self.authority, 'authority')
        self.validate_required(self.name, 'name')
        self.validate_required(self.birth, 'birth')
        self.validate_required(self.back_image_url, 'back_image_url')
        self.validate_required(self.start_date, 'start_date')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number is not None:
            result['Number'] = self.number
        if self.address is not None:
            result['Address'] = self.address
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.front_image_url is not None:
            result['FrontImageUrl'] = self.front_image_url
        if self.authority is not None:
            result['Authority'] = self.authority
        if self.name is not None:
            result['Name'] = self.name
        if self.birth is not None:
            result['Birth'] = self.birth
        if self.back_image_url is not None:
            result['BackImageUrl'] = self.back_image_url
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('FrontImageUrl') is not None:
            self.front_image_url = m.get('FrontImageUrl')
        if m.get('Authority') is not None:
            self.authority = m.get('Authority')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Birth') is not None:
            self.birth = m.get('Birth')
        if m.get('BackImageUrl') is not None:
            self.back_image_url = m.get('BackImageUrl')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class DescribeVerifyResultResponseMaterial(TeaModel):
    def __init__(
        self,
        face_image_url: str = None,
        id_card_name: str = None,
        id_card_number: str = None,
        face_quality: str = None,
        face_global_url: str = None,
        face_mask: bool = None,
        id_card_info: DescribeVerifyResultResponseMaterialIdCardInfo = None,
        video_urls: List[str] = None,
    ):
        self.face_image_url = face_image_url
        self.id_card_name = id_card_name
        self.id_card_number = id_card_number
        self.face_quality = face_quality
        self.face_global_url = face_global_url
        self.face_mask = face_mask
        self.id_card_info = id_card_info
        self.video_urls = video_urls

    def validate(self):
        self.validate_required(self.face_image_url, 'face_image_url')
        self.validate_required(self.id_card_name, 'id_card_name')
        self.validate_required(self.id_card_number, 'id_card_number')
        self.validate_required(self.face_quality, 'face_quality')
        self.validate_required(self.face_global_url, 'face_global_url')
        self.validate_required(self.face_mask, 'face_mask')
        self.validate_required(self.id_card_info, 'id_card_info')
        if self.id_card_info:
            self.id_card_info.validate()
        self.validate_required(self.video_urls, 'video_urls')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        if self.face_global_url is not None:
            result['FaceGlobalUrl'] = self.face_global_url
        if self.face_mask is not None:
            result['FaceMask'] = self.face_mask
        if self.id_card_info is not None:
            result['IdCardInfo'] = self.id_card_info.to_map()
        if self.video_urls is not None:
            result['VideoUrls'] = self.video_urls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        if m.get('FaceGlobalUrl') is not None:
            self.face_global_url = m.get('FaceGlobalUrl')
        if m.get('FaceMask') is not None:
            self.face_mask = m.get('FaceMask')
        if m.get('IdCardInfo') is not None:
            temp_model = DescribeVerifyResultResponseMaterialIdCardInfo()
            self.id_card_info = temp_model.from_map(m['IdCardInfo'])
        if m.get('VideoUrls') is not None:
            self.video_urls = m.get('VideoUrls')
        return self


class DescribeVerifyResultResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        verify_status: int = None,
        authority_comparision_score: float = None,
        face_comparison_score: float = None,
        id_card_face_comparison_score: float = None,
        material: DescribeVerifyResultResponseMaterial = None,
    ):
        self.request_id = request_id
        self.verify_status = verify_status
        self.authority_comparision_score = authority_comparision_score
        self.face_comparison_score = face_comparison_score
        self.id_card_face_comparison_score = id_card_face_comparison_score
        self.material = material

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.verify_status, 'verify_status')
        self.validate_required(self.authority_comparision_score, 'authority_comparision_score')
        self.validate_required(self.face_comparison_score, 'face_comparison_score')
        self.validate_required(self.id_card_face_comparison_score, 'id_card_face_comparison_score')
        self.validate_required(self.material, 'material')
        if self.material:
            self.material.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.verify_status is not None:
            result['VerifyStatus'] = self.verify_status
        if self.authority_comparision_score is not None:
            result['AuthorityComparisionScore'] = self.authority_comparision_score
        if self.face_comparison_score is not None:
            result['FaceComparisonScore'] = self.face_comparison_score
        if self.id_card_face_comparison_score is not None:
            result['IdCardFaceComparisonScore'] = self.id_card_face_comparison_score
        if self.material is not None:
            result['Material'] = self.material.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VerifyStatus') is not None:
            self.verify_status = m.get('VerifyStatus')
        if m.get('AuthorityComparisionScore') is not None:
            self.authority_comparision_score = m.get('AuthorityComparisionScore')
        if m.get('FaceComparisonScore') is not None:
            self.face_comparison_score = m.get('FaceComparisonScore')
        if m.get('IdCardFaceComparisonScore') is not None:
            self.id_card_face_comparison_score = m.get('IdCardFaceComparisonScore')
        if m.get('Material') is not None:
            temp_model = DescribeVerifyResultResponseMaterial()
            self.material = temp_model.from_map(m['Material'])
        return self


class DescribeOssUploadTokenRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DescribeOssUploadTokenResponseOssUploadToken(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        end_point: str = None,
        path: str = None,
        expired: int = None,
        secret: str = None,
        key: str = None,
        token: str = None,
    ):
        self.bucket = bucket
        self.end_point = end_point
        self.path = path
        self.expired = expired
        self.secret = secret
        self.key = key
        self.token = token

    def validate(self):
        self.validate_required(self.bucket, 'bucket')
        self.validate_required(self.end_point, 'end_point')
        self.validate_required(self.path, 'path')
        self.validate_required(self.expired, 'expired')
        self.validate_required(self.secret, 'secret')
        self.validate_required(self.key, 'key')
        self.validate_required(self.token, 'token')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.path is not None:
            result['Path'] = self.path
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.secret is not None:
            result['Secret'] = self.secret
        if self.key is not None:
            result['Key'] = self.key
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Secret') is not None:
            self.secret = m.get('Secret')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class DescribeOssUploadTokenResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        oss_upload_token: DescribeOssUploadTokenResponseOssUploadToken = None,
    ):
        self.request_id = request_id
        self.oss_upload_token = oss_upload_token

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.oss_upload_token, 'oss_upload_token')
        if self.oss_upload_token:
            self.oss_upload_token.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.oss_upload_token is not None:
            result['OssUploadToken'] = self.oss_upload_token.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OssUploadToken') is not None:
            temp_model = DescribeOssUploadTokenResponseOssUploadToken()
            self.oss_upload_token = temp_model.from_map(m['OssUploadToken'])
        return self


class DescribeVerifyTokenRequest(TeaModel):
    def __init__(
        self,
        id_card_back_image_url: str = None,
        biz_type: str = None,
        failed_redirect_url: str = None,
        face_retained_image_url: str = None,
        callback_seed: str = None,
        id_card_front_image_url: str = None,
        user_id: str = None,
        biz_id: str = None,
        name: str = None,
        id_card_number: str = None,
        passed_redirect_url: str = None,
        callback_url: str = None,
        user_ip: str = None,
        user_phone_number: str = None,
        user_regist_time: int = None,
    ):
        self.id_card_back_image_url = id_card_back_image_url
        self.biz_type = biz_type
        self.failed_redirect_url = failed_redirect_url
        self.face_retained_image_url = face_retained_image_url
        self.callback_seed = callback_seed
        self.id_card_front_image_url = id_card_front_image_url
        self.user_id = user_id
        self.biz_id = biz_id
        self.name = name
        self.id_card_number = id_card_number
        self.passed_redirect_url = passed_redirect_url
        self.callback_url = callback_url
        self.user_ip = user_ip
        self.user_phone_number = user_phone_number
        self.user_regist_time = user_regist_time

    def validate(self):
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.biz_id, 'biz_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id_card_back_image_url is not None:
            result['IdCardBackImageUrl'] = self.id_card_back_image_url
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.failed_redirect_url is not None:
            result['FailedRedirectUrl'] = self.failed_redirect_url
        if self.face_retained_image_url is not None:
            result['FaceRetainedImageUrl'] = self.face_retained_image_url
        if self.callback_seed is not None:
            result['CallbackSeed'] = self.callback_seed
        if self.id_card_front_image_url is not None:
            result['IdCardFrontImageUrl'] = self.id_card_front_image_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.name is not None:
            result['Name'] = self.name
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.passed_redirect_url is not None:
            result['PassedRedirectUrl'] = self.passed_redirect_url
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.user_ip is not None:
            result['UserIp'] = self.user_ip
        if self.user_phone_number is not None:
            result['UserPhoneNumber'] = self.user_phone_number
        if self.user_regist_time is not None:
            result['UserRegistTime'] = self.user_regist_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdCardBackImageUrl') is not None:
            self.id_card_back_image_url = m.get('IdCardBackImageUrl')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('FailedRedirectUrl') is not None:
            self.failed_redirect_url = m.get('FailedRedirectUrl')
        if m.get('FaceRetainedImageUrl') is not None:
            self.face_retained_image_url = m.get('FaceRetainedImageUrl')
        if m.get('CallbackSeed') is not None:
            self.callback_seed = m.get('CallbackSeed')
        if m.get('IdCardFrontImageUrl') is not None:
            self.id_card_front_image_url = m.get('IdCardFrontImageUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('PassedRedirectUrl') is not None:
            self.passed_redirect_url = m.get('PassedRedirectUrl')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('UserIp') is not None:
            self.user_ip = m.get('UserIp')
        if m.get('UserPhoneNumber') is not None:
            self.user_phone_number = m.get('UserPhoneNumber')
        if m.get('UserRegistTime') is not None:
            self.user_regist_time = m.get('UserRegistTime')
        return self


class DescribeVerifyTokenResponseOssUploadToken(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        end_point: str = None,
        path: str = None,
        expired: int = None,
        secret: str = None,
        key: str = None,
        token: str = None,
    ):
        self.bucket = bucket
        self.end_point = end_point
        self.path = path
        self.expired = expired
        self.secret = secret
        self.key = key
        self.token = token

    def validate(self):
        self.validate_required(self.bucket, 'bucket')
        self.validate_required(self.end_point, 'end_point')
        self.validate_required(self.path, 'path')
        self.validate_required(self.expired, 'expired')
        self.validate_required(self.secret, 'secret')
        self.validate_required(self.key, 'key')
        self.validate_required(self.token, 'token')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.path is not None:
            result['Path'] = self.path
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.secret is not None:
            result['Secret'] = self.secret
        if self.key is not None:
            result['Key'] = self.key
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Secret') is not None:
            self.secret = m.get('Secret')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class DescribeVerifyTokenResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        verify_page_url: str = None,
        verify_token: str = None,
        oss_upload_token: DescribeVerifyTokenResponseOssUploadToken = None,
    ):
        self.request_id = request_id
        self.verify_page_url = verify_page_url
        self.verify_token = verify_token
        self.oss_upload_token = oss_upload_token

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.verify_page_url, 'verify_page_url')
        self.validate_required(self.verify_token, 'verify_token')
        self.validate_required(self.oss_upload_token, 'oss_upload_token')
        if self.oss_upload_token:
            self.oss_upload_token.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.verify_page_url is not None:
            result['VerifyPageUrl'] = self.verify_page_url
        if self.verify_token is not None:
            result['VerifyToken'] = self.verify_token
        if self.oss_upload_token is not None:
            result['OssUploadToken'] = self.oss_upload_token.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VerifyPageUrl') is not None:
            self.verify_page_url = m.get('VerifyPageUrl')
        if m.get('VerifyToken') is not None:
            self.verify_token = m.get('VerifyToken')
        if m.get('OssUploadToken') is not None:
            temp_model = DescribeVerifyTokenResponseOssUploadToken()
            self.oss_upload_token = temp_model.from_map(m['OssUploadToken'])
        return self


