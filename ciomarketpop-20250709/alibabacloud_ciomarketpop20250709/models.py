# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class GetEveryOneSellsFormListRequest(TeaModel):
    def __init__(
        self,
        auth: str = None,
    ):
        self.auth = auth

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth is not None:
            result['Auth'] = self.auth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Auth') is not None:
            self.auth = m.get('Auth')
        return self


class GetEveryOneSellsFormListResponseBody(TeaModel):
    def __init__(
        self,
        id: int = None,
        virtual_main_department: str = None,
        virtual_department_name: str = None,
        virtual_department_code: str = None,
        virtual_parent_department: str = None,
        virtual_department_status: str = None,
        ding_id: str = None,
        emp_status: str = None,
    ):
        self.id = id
        self.virtual_main_department = virtual_main_department
        self.virtual_department_name = virtual_department_name
        self.virtual_department_code = virtual_department_code
        self.virtual_parent_department = virtual_parent_department
        self.virtual_department_status = virtual_department_status
        self.ding_id = ding_id
        self.emp_status = emp_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.virtual_main_department is not None:
            result['VirtualMainDepartment'] = self.virtual_main_department
        if self.virtual_department_name is not None:
            result['VirtualDepartmentName'] = self.virtual_department_name
        if self.virtual_department_code is not None:
            result['VirtualDepartmentCode'] = self.virtual_department_code
        if self.virtual_parent_department is not None:
            result['VirtualParentDepartment'] = self.virtual_parent_department
        if self.virtual_department_status is not None:
            result['VirtualDepartmentStatus'] = self.virtual_department_status
        if self.ding_id is not None:
            result['DingId'] = self.ding_id
        if self.emp_status is not None:
            result['EmpStatus'] = self.emp_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('VirtualMainDepartment') is not None:
            self.virtual_main_department = m.get('VirtualMainDepartment')
        if m.get('VirtualDepartmentName') is not None:
            self.virtual_department_name = m.get('VirtualDepartmentName')
        if m.get('VirtualDepartmentCode') is not None:
            self.virtual_department_code = m.get('VirtualDepartmentCode')
        if m.get('VirtualParentDepartment') is not None:
            self.virtual_parent_department = m.get('VirtualParentDepartment')
        if m.get('VirtualDepartmentStatus') is not None:
            self.virtual_department_status = m.get('VirtualDepartmentStatus')
        if m.get('DingId') is not None:
            self.ding_id = m.get('DingId')
        if m.get('EmpStatus') is not None:
            self.emp_status = m.get('EmpStatus')
        return self


class GetEveryOneSellsFormListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[GetEveryOneSellsFormListResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = GetEveryOneSellsFormListResponseBody()
                self.body.append(temp_model.from_map(k))
        return self


class PushEveryOneSellMsgRequest(TeaModel):
    def __init__(
        self,
        ding_id_list: List[str] = None,
        push_msg: str = None,
        push_type: str = None,
    ):
        self.ding_id_list = ding_id_list
        self.push_msg = push_msg
        self.push_type = push_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ding_id_list is not None:
            result['DingIdList'] = self.ding_id_list
        if self.push_msg is not None:
            result['PushMsg'] = self.push_msg
        if self.push_type is not None:
            result['PushType'] = self.push_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DingIdList') is not None:
            self.ding_id_list = m.get('DingIdList')
        if m.get('PushMsg') is not None:
            self.push_msg = m.get('PushMsg')
        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')
        return self


class PushEveryOneSellMsgShrinkRequest(TeaModel):
    def __init__(
        self,
        ding_id_list_shrink: str = None,
        push_msg: str = None,
        push_type: str = None,
    ):
        self.ding_id_list_shrink = ding_id_list_shrink
        self.push_msg = push_msg
        self.push_type = push_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ding_id_list_shrink is not None:
            result['DingIdList'] = self.ding_id_list_shrink
        if self.push_msg is not None:
            result['PushMsg'] = self.push_msg
        if self.push_type is not None:
            result['PushType'] = self.push_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DingIdList') is not None:
            self.ding_id_list_shrink = m.get('DingIdList')
        if m.get('PushMsg') is not None:
            self.push_msg = m.get('PushMsg')
        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')
        return self


class PushEveryOneSellMsgResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: str = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        pass

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
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


