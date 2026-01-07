# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_accountcenter20241209 import models as main_models
from darabonba.model import DaraModel

class EnterpriseTodoQueryAccountTodoListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.EnterpriseTodoQueryAccountTodoListResponseBodyData = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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
            temp_model = main_models.EnterpriseTodoQueryAccountTodoListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class EnterpriseTodoQueryAccountTodoListResponseBodyData(DaraModel):
    def __init__(
        self,
        count: int = None,
        todo_list: List[main_models.EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoList] = None,
    ):
        self.count = count
        self.todo_list = todo_list

    def validate(self):
        if self.todo_list:
            for v1 in self.todo_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['TodoList'] = []
        if self.todo_list is not None:
            for k1 in self.todo_list:
                result['TodoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.todo_list = []
        if m.get('TodoList') is not None:
            for k1 in m.get('TodoList'):
                temp_model = main_models.EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoList()
                self.todo_list.append(temp_model.from_map(k1))

        return self

class EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoList(DaraModel):
    def __init__(
        self,
        aliyun_id: str = None,
        applicant_aliyun_id: str = None,
        applicant_pk: str = None,
        apply_remark: str = None,
        apply_time: int = None,
        auditor_aliyun_id: str = None,
        auditor_pk: str = None,
        auditor_status: str = None,
        canceled_time: int = None,
        closed: bool = None,
        curr_auditor: bool = None,
        from_le: main_models.EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListFromLe = None,
        pk: str = None,
        process_list: List[main_models.EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListProcessList] = None,
        status: str = None,
        timeout_time: int = None,
        to_le: main_models.EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListToLe = None,
        to_le_audit: bool = None,
        todo_id: str = None,
        todo_type: str = None,
        todo_view: str = None,
    ):
        self.aliyun_id = aliyun_id
        self.applicant_aliyun_id = applicant_aliyun_id
        self.applicant_pk = applicant_pk
        self.apply_remark = apply_remark
        self.apply_time = apply_time
        self.auditor_aliyun_id = auditor_aliyun_id
        self.auditor_pk = auditor_pk
        self.auditor_status = auditor_status
        self.canceled_time = canceled_time
        self.closed = closed
        self.curr_auditor = curr_auditor
        self.from_le = from_le
        self.pk = pk
        self.process_list = process_list
        self.status = status
        self.timeout_time = timeout_time
        self.to_le = to_le
        self.to_le_audit = to_le_audit
        self.todo_id = todo_id
        self.todo_type = todo_type
        self.todo_view = todo_view

    def validate(self):
        if self.from_le:
            self.from_le.validate()
        if self.process_list:
            for v1 in self.process_list:
                 if v1:
                    v1.validate()
        if self.to_le:
            self.to_le.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id

        if self.applicant_aliyun_id is not None:
            result['ApplicantAliyunId'] = self.applicant_aliyun_id

        if self.applicant_pk is not None:
            result['ApplicantPk'] = self.applicant_pk

        if self.apply_remark is not None:
            result['ApplyRemark'] = self.apply_remark

        if self.apply_time is not None:
            result['ApplyTime'] = self.apply_time

        if self.auditor_aliyun_id is not None:
            result['AuditorAliyunId'] = self.auditor_aliyun_id

        if self.auditor_pk is not None:
            result['AuditorPk'] = self.auditor_pk

        if self.auditor_status is not None:
            result['AuditorStatus'] = self.auditor_status

        if self.canceled_time is not None:
            result['CanceledTime'] = self.canceled_time

        if self.closed is not None:
            result['Closed'] = self.closed

        if self.curr_auditor is not None:
            result['CurrAuditor'] = self.curr_auditor

        if self.from_le is not None:
            result['FromLe'] = self.from_le.to_map()

        if self.pk is not None:
            result['Pk'] = self.pk

        result['ProcessList'] = []
        if self.process_list is not None:
            for k1 in self.process_list:
                result['ProcessList'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.timeout_time is not None:
            result['TimeoutTime'] = self.timeout_time

        if self.to_le is not None:
            result['ToLe'] = self.to_le.to_map()

        if self.to_le_audit is not None:
            result['ToLeAudit'] = self.to_le_audit

        if self.todo_id is not None:
            result['TodoId'] = self.todo_id

        if self.todo_type is not None:
            result['TodoType'] = self.todo_type

        if self.todo_view is not None:
            result['TodoView'] = self.todo_view

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')

        if m.get('ApplicantAliyunId') is not None:
            self.applicant_aliyun_id = m.get('ApplicantAliyunId')

        if m.get('ApplicantPk') is not None:
            self.applicant_pk = m.get('ApplicantPk')

        if m.get('ApplyRemark') is not None:
            self.apply_remark = m.get('ApplyRemark')

        if m.get('ApplyTime') is not None:
            self.apply_time = m.get('ApplyTime')

        if m.get('AuditorAliyunId') is not None:
            self.auditor_aliyun_id = m.get('AuditorAliyunId')

        if m.get('AuditorPk') is not None:
            self.auditor_pk = m.get('AuditorPk')

        if m.get('AuditorStatus') is not None:
            self.auditor_status = m.get('AuditorStatus')

        if m.get('CanceledTime') is not None:
            self.canceled_time = m.get('CanceledTime')

        if m.get('Closed') is not None:
            self.closed = m.get('Closed')

        if m.get('CurrAuditor') is not None:
            self.curr_auditor = m.get('CurrAuditor')

        if m.get('FromLe') is not None:
            temp_model = main_models.EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListFromLe()
            self.from_le = temp_model.from_map(m.get('FromLe'))

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        self.process_list = []
        if m.get('ProcessList') is not None:
            for k1 in m.get('ProcessList'):
                temp_model = main_models.EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListProcessList()
                self.process_list.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimeoutTime') is not None:
            self.timeout_time = m.get('TimeoutTime')

        if m.get('ToLe') is not None:
            temp_model = main_models.EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListToLe()
            self.to_le = temp_model.from_map(m.get('ToLe'))

        if m.get('ToLeAudit') is not None:
            self.to_le_audit = m.get('ToLeAudit')

        if m.get('TodoId') is not None:
            self.todo_id = m.get('TodoId')

        if m.get('TodoType') is not None:
            self.todo_type = m.get('TodoType')

        if m.get('TodoView') is not None:
            self.todo_view = m.get('TodoView')

        return self

class EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListToLe(DaraModel):
    def __init__(
        self,
        ec_id: str = None,
        le_id: str = None,
        license_number: str = None,
        manageable_account_count: int = None,
        managed_account_count: int = None,
        manager_list: List[main_models.EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListToLeManagerList] = None,
        nb_id: str = None,
        subject_name: str = None,
        subject_type: str = None,
    ):
        self.ec_id = ec_id
        self.le_id = le_id
        self.license_number = license_number
        self.manageable_account_count = manageable_account_count
        self.managed_account_count = managed_account_count
        self.manager_list = manager_list
        self.nb_id = nb_id
        self.subject_name = subject_name
        self.subject_type = subject_type

    def validate(self):
        if self.manager_list:
            for v1 in self.manager_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ec_id is not None:
            result['EcId'] = self.ec_id

        if self.le_id is not None:
            result['LeId'] = self.le_id

        if self.license_number is not None:
            result['LicenseNumber'] = self.license_number

        if self.manageable_account_count is not None:
            result['ManageableAccountCount'] = self.manageable_account_count

        if self.managed_account_count is not None:
            result['ManagedAccountCount'] = self.managed_account_count

        result['ManagerList'] = []
        if self.manager_list is not None:
            for k1 in self.manager_list:
                result['ManagerList'].append(k1.to_map() if k1 else None)

        if self.nb_id is not None:
            result['NbId'] = self.nb_id

        if self.subject_name is not None:
            result['SubjectName'] = self.subject_name

        if self.subject_type is not None:
            result['SubjectType'] = self.subject_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')

        if m.get('LeId') is not None:
            self.le_id = m.get('LeId')

        if m.get('LicenseNumber') is not None:
            self.license_number = m.get('LicenseNumber')

        if m.get('ManageableAccountCount') is not None:
            self.manageable_account_count = m.get('ManageableAccountCount')

        if m.get('ManagedAccountCount') is not None:
            self.managed_account_count = m.get('ManagedAccountCount')

        self.manager_list = []
        if m.get('ManagerList') is not None:
            for k1 in m.get('ManagerList'):
                temp_model = main_models.EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListToLeManagerList()
                self.manager_list.append(temp_model.from_map(k1))

        if m.get('NbId') is not None:
            self.nb_id = m.get('NbId')

        if m.get('SubjectName') is not None:
            self.subject_name = m.get('SubjectName')

        if m.get('SubjectType') is not None:
            self.subject_type = m.get('SubjectType')

        return self

class EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListToLeManagerList(DaraModel):
    def __init__(
        self,
        aliyun_id: str = None,
        pk: str = None,
        pk_encoded: str = None,
        role: str = None,
    ):
        self.aliyun_id = aliyun_id
        self.pk = pk
        self.pk_encoded = pk_encoded
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id

        if self.pk is not None:
            result['Pk'] = self.pk

        if self.pk_encoded is not None:
            result['PkEncoded'] = self.pk_encoded

        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        if m.get('PkEncoded') is not None:
            self.pk_encoded = m.get('PkEncoded')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

class EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListProcessList(DaraModel):
    def __init__(
        self,
        aliyun_id: str = None,
        audit_time: int = None,
        ec_id: str = None,
        le_id: str = None,
        nb_id: str = None,
        pk: str = None,
        remark: str = None,
        status: str = None,
    ):
        self.aliyun_id = aliyun_id
        self.audit_time = audit_time
        self.ec_id = ec_id
        self.le_id = le_id
        self.nb_id = nb_id
        self.pk = pk
        self.remark = remark
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id

        if self.audit_time is not None:
            result['AuditTime'] = self.audit_time

        if self.ec_id is not None:
            result['EcId'] = self.ec_id

        if self.le_id is not None:
            result['LeId'] = self.le_id

        if self.nb_id is not None:
            result['NbId'] = self.nb_id

        if self.pk is not None:
            result['Pk'] = self.pk

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')

        if m.get('AuditTime') is not None:
            self.audit_time = m.get('AuditTime')

        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')

        if m.get('LeId') is not None:
            self.le_id = m.get('LeId')

        if m.get('NbId') is not None:
            self.nb_id = m.get('NbId')

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListFromLe(DaraModel):
    def __init__(
        self,
        ec_id: str = None,
        le_id: str = None,
        license_number: str = None,
        manageable_account_count: int = None,
        managed_account_count: int = None,
        manager_list: List[main_models.EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListFromLeManagerList] = None,
        nb_id: str = None,
        subject_name: str = None,
        subject_type: str = None,
    ):
        self.ec_id = ec_id
        self.le_id = le_id
        self.license_number = license_number
        self.manageable_account_count = manageable_account_count
        self.managed_account_count = managed_account_count
        self.manager_list = manager_list
        self.nb_id = nb_id
        self.subject_name = subject_name
        self.subject_type = subject_type

    def validate(self):
        if self.manager_list:
            for v1 in self.manager_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ec_id is not None:
            result['EcId'] = self.ec_id

        if self.le_id is not None:
            result['LeId'] = self.le_id

        if self.license_number is not None:
            result['LicenseNumber'] = self.license_number

        if self.manageable_account_count is not None:
            result['ManageableAccountCount'] = self.manageable_account_count

        if self.managed_account_count is not None:
            result['ManagedAccountCount'] = self.managed_account_count

        result['ManagerList'] = []
        if self.manager_list is not None:
            for k1 in self.manager_list:
                result['ManagerList'].append(k1.to_map() if k1 else None)

        if self.nb_id is not None:
            result['NbId'] = self.nb_id

        if self.subject_name is not None:
            result['SubjectName'] = self.subject_name

        if self.subject_type is not None:
            result['SubjectType'] = self.subject_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')

        if m.get('LeId') is not None:
            self.le_id = m.get('LeId')

        if m.get('LicenseNumber') is not None:
            self.license_number = m.get('LicenseNumber')

        if m.get('ManageableAccountCount') is not None:
            self.manageable_account_count = m.get('ManageableAccountCount')

        if m.get('ManagedAccountCount') is not None:
            self.managed_account_count = m.get('ManagedAccountCount')

        self.manager_list = []
        if m.get('ManagerList') is not None:
            for k1 in m.get('ManagerList'):
                temp_model = main_models.EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListFromLeManagerList()
                self.manager_list.append(temp_model.from_map(k1))

        if m.get('NbId') is not None:
            self.nb_id = m.get('NbId')

        if m.get('SubjectName') is not None:
            self.subject_name = m.get('SubjectName')

        if m.get('SubjectType') is not None:
            self.subject_type = m.get('SubjectType')

        return self

class EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListFromLeManagerList(DaraModel):
    def __init__(
        self,
        aliyun_id: str = None,
        pk: str = None,
        pk_encoded: str = None,
        role: str = None,
    ):
        self.aliyun_id = aliyun_id
        self.pk = pk
        self.pk_encoded = pk_encoded
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id

        if self.pk is not None:
            result['Pk'] = self.pk

        if self.pk_encoded is not None:
            result['PkEncoded'] = self.pk_encoded

        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        if m.get('PkEncoded') is not None:
            self.pk_encoded = m.get('PkEncoded')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

