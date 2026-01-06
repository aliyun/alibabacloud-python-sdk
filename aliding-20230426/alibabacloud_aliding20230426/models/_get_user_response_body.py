# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetUserResponseBody(DaraModel):
    def __init__(
        self,
        active: bool = None,
        admin: bool = None,
        avatar: str = None,
        boss: bool = None,
        dept_id_list: List[int] = None,
        dept_order_list: List[main_models.GetUserResponseBodyDeptOrderList] = None,
        email: str = None,
        exclusive_account: bool = None,
        exclusive_account_corp_id: str = None,
        exclusive_account_corp_name: str = None,
        exclusive_account_type: str = None,
        extension: str = None,
        hide_mobile: bool = None,
        hired_date: int = None,
        job_number: str = None,
        leader_in_dept: List[main_models.GetUserResponseBodyLeaderInDept] = None,
        login_id: str = None,
        manager_userid: str = None,
        mobile: str = None,
        name: str = None,
        nickname: str = None,
        org_email: str = None,
        real_authed: bool = None,
        remark: str = None,
        request_id: str = None,
        role_list: List[main_models.GetUserResponseBodyRoleList] = None,
        senior: bool = None,
        state_code: str = None,
        telephone: str = None,
        title: str = None,
        union_emp_ext: main_models.GetUserResponseBodyUnionEmpExt = None,
        unionid: str = None,
        userid: str = None,
        work_place: str = None,
    ):
        self.active = active
        self.admin = admin
        self.avatar = avatar
        self.boss = boss
        self.dept_id_list = dept_id_list
        self.dept_order_list = dept_order_list
        self.email = email
        self.exclusive_account = exclusive_account
        self.exclusive_account_corp_id = exclusive_account_corp_id
        self.exclusive_account_corp_name = exclusive_account_corp_name
        self.exclusive_account_type = exclusive_account_type
        self.extension = extension
        self.hide_mobile = hide_mobile
        self.hired_date = hired_date
        self.job_number = job_number
        self.leader_in_dept = leader_in_dept
        self.login_id = login_id
        self.manager_userid = manager_userid
        self.mobile = mobile
        self.name = name
        self.nickname = nickname
        self.org_email = org_email
        self.real_authed = real_authed
        self.remark = remark
        self.request_id = request_id
        self.role_list = role_list
        self.senior = senior
        self.state_code = state_code
        self.telephone = telephone
        self.title = title
        self.union_emp_ext = union_emp_ext
        self.unionid = unionid
        self.userid = userid
        self.work_place = work_place

    def validate(self):
        if self.dept_order_list:
            for v1 in self.dept_order_list:
                 if v1:
                    v1.validate()
        if self.leader_in_dept:
            for v1 in self.leader_in_dept:
                 if v1:
                    v1.validate()
        if self.role_list:
            for v1 in self.role_list:
                 if v1:
                    v1.validate()
        if self.union_emp_ext:
            self.union_emp_ext.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['active'] = self.active

        if self.admin is not None:
            result['admin'] = self.admin

        if self.avatar is not None:
            result['avatar'] = self.avatar

        if self.boss is not None:
            result['boss'] = self.boss

        if self.dept_id_list is not None:
            result['deptIdList'] = self.dept_id_list

        result['deptOrderList'] = []
        if self.dept_order_list is not None:
            for k1 in self.dept_order_list:
                result['deptOrderList'].append(k1.to_map() if k1 else None)

        if self.email is not None:
            result['email'] = self.email

        if self.exclusive_account is not None:
            result['exclusiveAccount'] = self.exclusive_account

        if self.exclusive_account_corp_id is not None:
            result['exclusiveAccountCorpId'] = self.exclusive_account_corp_id

        if self.exclusive_account_corp_name is not None:
            result['exclusiveAccountCorpName'] = self.exclusive_account_corp_name

        if self.exclusive_account_type is not None:
            result['exclusiveAccountType'] = self.exclusive_account_type

        if self.extension is not None:
            result['extension'] = self.extension

        if self.hide_mobile is not None:
            result['hideMobile'] = self.hide_mobile

        if self.hired_date is not None:
            result['hiredDate'] = self.hired_date

        if self.job_number is not None:
            result['jobNumber'] = self.job_number

        result['leaderInDept'] = []
        if self.leader_in_dept is not None:
            for k1 in self.leader_in_dept:
                result['leaderInDept'].append(k1.to_map() if k1 else None)

        if self.login_id is not None:
            result['loginId'] = self.login_id

        if self.manager_userid is not None:
            result['managerUserid'] = self.manager_userid

        if self.mobile is not None:
            result['mobile'] = self.mobile

        if self.name is not None:
            result['name'] = self.name

        if self.nickname is not None:
            result['nickname'] = self.nickname

        if self.org_email is not None:
            result['orgEmail'] = self.org_email

        if self.real_authed is not None:
            result['realAuthed'] = self.real_authed

        if self.remark is not None:
            result['remark'] = self.remark

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['roleList'] = []
        if self.role_list is not None:
            for k1 in self.role_list:
                result['roleList'].append(k1.to_map() if k1 else None)

        if self.senior is not None:
            result['senior'] = self.senior

        if self.state_code is not None:
            result['stateCode'] = self.state_code

        if self.telephone is not None:
            result['telephone'] = self.telephone

        if self.title is not None:
            result['title'] = self.title

        if self.union_emp_ext is not None:
            result['unionEmpExt'] = self.union_emp_ext.to_map()

        if self.unionid is not None:
            result['unionid'] = self.unionid

        if self.userid is not None:
            result['userid'] = self.userid

        if self.work_place is not None:
            result['workPlace'] = self.work_place

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')

        if m.get('admin') is not None:
            self.admin = m.get('admin')

        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')

        if m.get('boss') is not None:
            self.boss = m.get('boss')

        if m.get('deptIdList') is not None:
            self.dept_id_list = m.get('deptIdList')

        self.dept_order_list = []
        if m.get('deptOrderList') is not None:
            for k1 in m.get('deptOrderList'):
                temp_model = main_models.GetUserResponseBodyDeptOrderList()
                self.dept_order_list.append(temp_model.from_map(k1))

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('exclusiveAccount') is not None:
            self.exclusive_account = m.get('exclusiveAccount')

        if m.get('exclusiveAccountCorpId') is not None:
            self.exclusive_account_corp_id = m.get('exclusiveAccountCorpId')

        if m.get('exclusiveAccountCorpName') is not None:
            self.exclusive_account_corp_name = m.get('exclusiveAccountCorpName')

        if m.get('exclusiveAccountType') is not None:
            self.exclusive_account_type = m.get('exclusiveAccountType')

        if m.get('extension') is not None:
            self.extension = m.get('extension')

        if m.get('hideMobile') is not None:
            self.hide_mobile = m.get('hideMobile')

        if m.get('hiredDate') is not None:
            self.hired_date = m.get('hiredDate')

        if m.get('jobNumber') is not None:
            self.job_number = m.get('jobNumber')

        self.leader_in_dept = []
        if m.get('leaderInDept') is not None:
            for k1 in m.get('leaderInDept'):
                temp_model = main_models.GetUserResponseBodyLeaderInDept()
                self.leader_in_dept.append(temp_model.from_map(k1))

        if m.get('loginId') is not None:
            self.login_id = m.get('loginId')

        if m.get('managerUserid') is not None:
            self.manager_userid = m.get('managerUserid')

        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nickname') is not None:
            self.nickname = m.get('nickname')

        if m.get('orgEmail') is not None:
            self.org_email = m.get('orgEmail')

        if m.get('realAuthed') is not None:
            self.real_authed = m.get('realAuthed')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.role_list = []
        if m.get('roleList') is not None:
            for k1 in m.get('roleList'):
                temp_model = main_models.GetUserResponseBodyRoleList()
                self.role_list.append(temp_model.from_map(k1))

        if m.get('senior') is not None:
            self.senior = m.get('senior')

        if m.get('stateCode') is not None:
            self.state_code = m.get('stateCode')

        if m.get('telephone') is not None:
            self.telephone = m.get('telephone')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('unionEmpExt') is not None:
            temp_model = main_models.GetUserResponseBodyUnionEmpExt()
            self.union_emp_ext = temp_model.from_map(m.get('unionEmpExt'))

        if m.get('unionid') is not None:
            self.unionid = m.get('unionid')

        if m.get('userid') is not None:
            self.userid = m.get('userid')

        if m.get('workPlace') is not None:
            self.work_place = m.get('workPlace')

        return self

class GetUserResponseBodyUnionEmpExt(DaraModel):
    def __init__(
        self,
        corp_id: str = None,
        union_emp_map_list: List[main_models.GetUserResponseBodyUnionEmpExtUnionEmpMapList] = None,
        userid: str = None,
    ):
        self.corp_id = corp_id
        self.union_emp_map_list = union_emp_map_list
        self.userid = userid

    def validate(self):
        if self.union_emp_map_list:
            for v1 in self.union_emp_map_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.corp_id is not None:
            result['corpId'] = self.corp_id

        result['unionEmpMapList'] = []
        if self.union_emp_map_list is not None:
            for k1 in self.union_emp_map_list:
                result['unionEmpMapList'].append(k1.to_map() if k1 else None)

        if self.userid is not None:
            result['userid'] = self.userid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')

        self.union_emp_map_list = []
        if m.get('unionEmpMapList') is not None:
            for k1 in m.get('unionEmpMapList'):
                temp_model = main_models.GetUserResponseBodyUnionEmpExtUnionEmpMapList()
                self.union_emp_map_list.append(temp_model.from_map(k1))

        if m.get('userid') is not None:
            self.userid = m.get('userid')

        return self

class GetUserResponseBodyUnionEmpExtUnionEmpMapList(DaraModel):
    def __init__(
        self,
        crop_id: str = None,
        userid: str = None,
    ):
        self.crop_id = crop_id
        self.userid = userid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.crop_id is not None:
            result['cropId'] = self.crop_id

        if self.userid is not None:
            result['userid'] = self.userid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cropId') is not None:
            self.crop_id = m.get('cropId')

        if m.get('userid') is not None:
            self.userid = m.get('userid')

        return self

class GetUserResponseBodyRoleList(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        id: int = None,
        name: str = None,
    ):
        self.group_name = group_name
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['groupName'] = self.group_name

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class GetUserResponseBodyLeaderInDept(DaraModel):
    def __init__(
        self,
        dept_id: int = None,
        leader: bool = None,
    ):
        self.dept_id = dept_id
        self.leader = leader

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dept_id is not None:
            result['deptId'] = self.dept_id

        if self.leader is not None:
            result['leader'] = self.leader

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deptId') is not None:
            self.dept_id = m.get('deptId')

        if m.get('leader') is not None:
            self.leader = m.get('leader')

        return self

class GetUserResponseBodyDeptOrderList(DaraModel):
    def __init__(
        self,
        dept_id: int = None,
        order: int = None,
    ):
        self.dept_id = dept_id
        self.order = order

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dept_id is not None:
            result['deptId'] = self.dept_id

        if self.order is not None:
            result['order'] = self.order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deptId') is not None:
            self.dept_id = m.get('deptId')

        if m.get('order') is not None:
            self.order = m.get('order')

        return self

