# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class QuerySmsQualificationRecordResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.QuerySmsQualificationRecordResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 访问被拒绝详细信息。
        self.access_denied_detail = access_denied_detail
        # 请求状态码。
        # 
        # * 返回OK代表请求成功。
        # * 其他错误码，请参见本章节的错误码列表或产品[API错误码](https://help.aliyun.com/document_detail/101346.html)。
        self.code = code
        # 资质审核列表
        self.data = data
        # 状态码的描述。
        self.message = message
        # 请求ID。
        self.request_id = request_id
        # 调用接口是否成功。取值：
        # 
        # - **true**：调用成功。
        # - **false**：调用失败。
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QuerySmsQualificationRecordResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QuerySmsQualificationRecordResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.QuerySmsQualificationRecordResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # 满足过滤条件的数据列表。
        self.list = list
        # 当前页码。
        self.page_no = page_no
        # 每页数据条数。
        self.page_size = page_size
        # 总条数。
        self.total = total

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.QuerySmsQualificationRecordResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class QuerySmsQualificationRecordResponseBodyDataList(DaraModel):
    def __init__(
        self,
        audit_remark: str = None,
        audit_time: str = None,
        company_name: str = None,
        create_date: str = None,
        group_id: int = None,
        legal_person_name: str = None,
        qualification_group_name: str = None,
        state_name: str = None,
        use_by_self: str = None,
        work_order_id: int = None,
    ):
        # 审核备注。
        self.audit_remark = audit_remark
        # 审核时间。
        self.audit_time = audit_time
        # 企业名称。
        self.company_name = company_name
        # 资质创建时间。
        self.create_date = create_date
        # 资质ID。
        self.group_id = group_id
        # 法人姓名。
        self.legal_person_name = legal_person_name
        # 资质名称。
        self.qualification_group_name = qualification_group_name
        # 审核状态。取值：
        # 
        # - INIT：审核中。
        # - NOT_PASS：审核不通过。 
        # - PASS：审核通过。
        # - NOT_FINISH：资料待补充。
        # - CANCEL：已撤回。
        self.state_name = state_name
        # 资质申请用途，取值：
        # 
        # - **true**：自用。
        # - **false**：他用。
        self.use_by_self = use_by_self
        # 审核工单ID。
        self.work_order_id = work_order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_remark is not None:
            result['AuditRemark'] = self.audit_remark

        if self.audit_time is not None:
            result['AuditTime'] = self.audit_time

        if self.company_name is not None:
            result['CompanyName'] = self.company_name

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.legal_person_name is not None:
            result['LegalPersonName'] = self.legal_person_name

        if self.qualification_group_name is not None:
            result['QualificationGroupName'] = self.qualification_group_name

        if self.state_name is not None:
            result['StateName'] = self.state_name

        if self.use_by_self is not None:
            result['UseBySelf'] = self.use_by_self

        if self.work_order_id is not None:
            result['WorkOrderId'] = self.work_order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditRemark') is not None:
            self.audit_remark = m.get('AuditRemark')

        if m.get('AuditTime') is not None:
            self.audit_time = m.get('AuditTime')

        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('LegalPersonName') is not None:
            self.legal_person_name = m.get('LegalPersonName')

        if m.get('QualificationGroupName') is not None:
            self.qualification_group_name = m.get('QualificationGroupName')

        if m.get('StateName') is not None:
            self.state_name = m.get('StateName')

        if m.get('UseBySelf') is not None:
            self.use_by_self = m.get('UseBySelf')

        if m.get('WorkOrderId') is not None:
            self.work_order_id = m.get('WorkOrderId')

        return self

