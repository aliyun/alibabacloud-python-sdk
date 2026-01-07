# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_accountcenter20241209 import models as main_models
from darabonba.model import DaraModel

class EnterpriseUninvitedAdminInviteJoinEnterpriseResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.EnterpriseUninvitedAdminInviteJoinEnterpriseResponseBodyData] = None,
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
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.EnterpriseUninvitedAdminInviteJoinEnterpriseResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class EnterpriseUninvitedAdminInviteJoinEnterpriseResponseBodyData(DaraModel):
    def __init__(
        self,
        applicant_aliyun_id: str = None,
        applicant_pk: str = None,
        apply_remark: str = None,
        apply_time: int = None,
        auditor_aliyun_id: str = None,
        auditor_pk: str = None,
        ec_id: str = None,
        le_id: str = None,
        le_license_no: str = None,
        le_name: str = None,
        message: str = None,
        nb_id: str = None,
        operated_aliyun_id: str = None,
        operated_pk: str = None,
        success: str = None,
        timeout_time: int = None,
        todo_id: str = None,
        todo_type: str = None,
    ):
        self.applicant_aliyun_id = applicant_aliyun_id
        self.applicant_pk = applicant_pk
        self.apply_remark = apply_remark
        self.apply_time = apply_time
        self.auditor_aliyun_id = auditor_aliyun_id
        self.auditor_pk = auditor_pk
        self.ec_id = ec_id
        self.le_id = le_id
        self.le_license_no = le_license_no
        self.le_name = le_name
        self.message = message
        self.nb_id = nb_id
        self.operated_aliyun_id = operated_aliyun_id
        self.operated_pk = operated_pk
        self.success = success
        self.timeout_time = timeout_time
        self.todo_id = todo_id
        self.todo_type = todo_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.ec_id is not None:
            result['EcId'] = self.ec_id

        if self.le_id is not None:
            result['LeId'] = self.le_id

        if self.le_license_no is not None:
            result['LeLicenseNo'] = self.le_license_no

        if self.le_name is not None:
            result['LeName'] = self.le_name

        if self.message is not None:
            result['Message'] = self.message

        if self.nb_id is not None:
            result['NbId'] = self.nb_id

        if self.operated_aliyun_id is not None:
            result['OperatedAliyunId'] = self.operated_aliyun_id

        if self.operated_pk is not None:
            result['OperatedPk'] = self.operated_pk

        if self.success is not None:
            result['Success'] = self.success

        if self.timeout_time is not None:
            result['TimeoutTime'] = self.timeout_time

        if self.todo_id is not None:
            result['TodoId'] = self.todo_id

        if self.todo_type is not None:
            result['TodoType'] = self.todo_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')

        if m.get('LeId') is not None:
            self.le_id = m.get('LeId')

        if m.get('LeLicenseNo') is not None:
            self.le_license_no = m.get('LeLicenseNo')

        if m.get('LeName') is not None:
            self.le_name = m.get('LeName')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NbId') is not None:
            self.nb_id = m.get('NbId')

        if m.get('OperatedAliyunId') is not None:
            self.operated_aliyun_id = m.get('OperatedAliyunId')

        if m.get('OperatedPk') is not None:
            self.operated_pk = m.get('OperatedPk')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TimeoutTime') is not None:
            self.timeout_time = m.get('TimeoutTime')

        if m.get('TodoId') is not None:
            self.todo_id = m.get('TodoId')

        if m.get('TodoType') is not None:
            self.todo_type = m.get('TodoType')

        return self

