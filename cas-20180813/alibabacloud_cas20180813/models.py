# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class ListPCAInstanceRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        show_size: int = None,
        type: str = None,
    ):
        self.current_page = current_page
        self.show_size = show_size
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListPCAInstanceResponseBodyPCAInstanceList(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        alias_name: str = None,
        ca_identifier: str = None,
        cert_count: int = None,
        end_time: int = None,
        instance_uuid: str = None,
        issued_cert_count: int = None,
        relate_status: bool = None,
        share_flag: int = None,
        trial: str = None,
    ):
        self.algorithm = algorithm
        self.alias_name = alias_name
        self.ca_identifier = ca_identifier
        self.cert_count = cert_count
        self.end_time = end_time
        self.instance_uuid = instance_uuid
        self.issued_cert_count = issued_cert_count
        self.relate_status = relate_status
        self.share_flag = share_flag
        self.trial = trial

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.ca_identifier is not None:
            result['CaIdentifier'] = self.ca_identifier
        if self.cert_count is not None:
            result['CertCount'] = self.cert_count
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_uuid is not None:
            result['InstanceUuid'] = self.instance_uuid
        if self.issued_cert_count is not None:
            result['IssuedCertCount'] = self.issued_cert_count
        if self.relate_status is not None:
            result['RelateStatus'] = self.relate_status
        if self.share_flag is not None:
            result['ShareFlag'] = self.share_flag
        if self.trial is not None:
            result['Trial'] = self.trial
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('CaIdentifier') is not None:
            self.ca_identifier = m.get('CaIdentifier')
        if m.get('CertCount') is not None:
            self.cert_count = m.get('CertCount')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceUuid') is not None:
            self.instance_uuid = m.get('InstanceUuid')
        if m.get('IssuedCertCount') is not None:
            self.issued_cert_count = m.get('IssuedCertCount')
        if m.get('RelateStatus') is not None:
            self.relate_status = m.get('RelateStatus')
        if m.get('ShareFlag') is not None:
            self.share_flag = m.get('ShareFlag')
        if m.get('Trial') is not None:
            self.trial = m.get('Trial')
        return self


class ListPCAInstanceResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        pcainstance_list: List[ListPCAInstanceResponseBodyPCAInstanceList] = None,
        request_id: str = None,
        show_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.pcainstance_list = pcainstance_list
        self.request_id = request_id
        self.show_size = show_size
        self.total_count = total_count

    def validate(self):
        if self.pcainstance_list:
            for k in self.pcainstance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['PCAInstanceList'] = []
        if self.pcainstance_list is not None:
            for k in self.pcainstance_list:
                result['PCAInstanceList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.show_size is not None:
            result['ShowSize'] = self.show_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.pcainstance_list = []
        if m.get('PCAInstanceList') is not None:
            for k in m.get('PCAInstanceList'):
                temp_model = ListPCAInstanceResponseBodyPCAInstanceList()
                self.pcainstance_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPCAInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPCAInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListPCAInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


