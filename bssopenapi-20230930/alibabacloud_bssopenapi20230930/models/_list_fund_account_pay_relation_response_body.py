# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class ListFundAccountPayRelationResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[main_models.ListFundAccountPayRelationResponseBodyData] = None,
        metadata: Any = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The current page number.
        self.current_page = current_page
        # The data list.
        self.data = data
        # The metadata of the response structure.
        self.metadata = metadata
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_count = total_count

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListFundAccountPayRelationResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListFundAccountPayRelationResponseBodyData(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        ecid: str = None,
        effective_time: str = None,
        fund_account_id: str = None,
        fund_account_owner_account_id: str = None,
        ineffective_time: str = None,
        nbid: str = None,
        operator_name: str = None,
        operator_no: str = None,
        operator_type: str = None,
        relation_type: str = None,
        site: str = None,
        status: str = None,
    ):
        # The account ID of the user associated with the payment relationship, which is the account that uses this account for payment.
        self.account_id = account_id
        # The username.
        self.account_name = account_name
        # The enterprise entity ID of the user associated with the payment relationship.
        self.ecid = ecid
        # The effective period of the payment relationship. The format is YYYY-MM-DD HH:mm:ss.
        self.effective_time = effective_time
        # The account ID.
        self.fund_account_id = fund_account_id
        # The Alibaba Cloud account ID of the account owner.
        self.fund_account_owner_account_id = fund_account_owner_account_id
        # The time when the payment relationship expires. The format is YYYY-MM-DD HH:mm:ss.
        self.ineffective_time = ineffective_time
        # The level-1 marketplace.
        self.nbid = nbid
        # The name of the operator. If the operator type is aliyun_pk, the value is the Alibaba Cloud nickname. If the operator type is system, the value is "Alibaba Cloud Support".
        self.operator_name = operator_name
        # The authorized operator. If the operator type is aliyun_pk, the value is the Alibaba Cloud account ID.
        self.operator_no = operator_no
        # The type of the authorized operator. Valid values:
        # - aliyun_pk: User.
        # - system: Alibaba Cloud system.
        self.operator_type = operator_type
        # The relationship type, which can be a collection relationship or a payment relationship.
        self.relation_type = relation_type
        # The site.
        self.site = site
        # The relationship status. Valid values:
        # - valid: Valid.
        # - expired: Invalid.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.ecid is not None:
            result['Ecid'] = self.ecid

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id

        if self.fund_account_owner_account_id is not None:
            result['FundAccountOwnerAccountId'] = self.fund_account_owner_account_id

        if self.ineffective_time is not None:
            result['IneffectiveTime'] = self.ineffective_time

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name

        if self.operator_no is not None:
            result['OperatorNo'] = self.operator_no

        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type

        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        if self.site is not None:
            result['Site'] = self.site

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('Ecid') is not None:
            self.ecid = m.get('Ecid')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')

        if m.get('FundAccountOwnerAccountId') is not None:
            self.fund_account_owner_account_id = m.get('FundAccountOwnerAccountId')

        if m.get('IneffectiveTime') is not None:
            self.ineffective_time = m.get('IneffectiveTime')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')

        if m.get('OperatorNo') is not None:
            self.operator_no = m.get('OperatorNo')

        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')

        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        if m.get('Site') is not None:
            self.site = m.get('Site')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

