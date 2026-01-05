# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySmsQualificationRecordRequest(DaraModel):
    def __init__(
        self,
        company_name: str = None,
        legal_person_name: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        qualification_group_name: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        state: str = None,
        use_by_self: bool = None,
        work_order_id: int = None,
    ):
        # 公司名
        self.company_name = company_name
        # 法人姓名
        self.legal_person_name = legal_person_name
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        # 资质组名称
        self.qualification_group_name = qualification_group_name
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 审核状态。INT:审核中FAILED:审核失败,PASSED:审核通过,NOT_FINISH:资料待补充,CANCELED:已撤回
        self.state = state
        # 是否自用
        self.use_by_self = use_by_self
        # 工单ID
        self.work_order_id = work_order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company_name is not None:
            result['CompanyName'] = self.company_name

        if self.legal_person_name is not None:
            result['LegalPersonName'] = self.legal_person_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.qualification_group_name is not None:
            result['QualificationGroupName'] = self.qualification_group_name

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.state is not None:
            result['State'] = self.state

        if self.use_by_self is not None:
            result['UseBySelf'] = self.use_by_self

        if self.work_order_id is not None:
            result['WorkOrderId'] = self.work_order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')

        if m.get('LegalPersonName') is not None:
            self.legal_person_name = m.get('LegalPersonName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QualificationGroupName') is not None:
            self.qualification_group_name = m.get('QualificationGroupName')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('UseBySelf') is not None:
            self.use_by_self = m.get('UseBySelf')

        if m.get('WorkOrderId') is not None:
            self.work_order_id = m.get('WorkOrderId')

        return self

