# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeDeductLogsRequest(DaraModel):
    def __init__(
        self,
        bill_instance_id: str = None,
        billing_commodity_code: str = None,
        billing_end_time: int = None,
        billing_start_time: int = None,
        commodity_code: str = None,
        ec_id_account_ids: List[main_models.DescribeDeductLogsRequestEcIdAccountIds] = None,
        group: str = None,
        instance_id: str = None,
        nbid: str = None,
        page_num: int = None,
        page_size: int = None,
        relation_account_ids: List[int] = None,
    ):
        # The instance ID for billing deduction.
        self.bill_instance_id = bill_instance_id
        # The commodity code of the deducted item.
        self.billing_commodity_code = billing_commodity_code
        # The billing end time.
        # 
        # This parameter is required.
        self.billing_end_time = billing_end_time
        # The billing start time.
        # 
        # This parameter is required.
        self.billing_start_time = billing_start_time
        # The commodity code.
        self.commodity_code = commodity_code
        # The enterprise and account list. If this parameter is empty, the current account is queried.
        self.ec_id_account_ids = ec_id_account_ids
        # The resource dimension for the query.
        self.group = group
        # The instance name.
        self.instance_id = instance_id
        # The primary marketplace ID. If this parameter is empty, the marketplace ID of the current user is used by default.
        self.nbid = nbid
        # The current page number.
        self.page_num = page_num
        # The number of entries per page.
        self.page_size = page_size
        # The list of deduction accounts.
        self.relation_account_ids = relation_account_ids

    def validate(self):
        if self.ec_id_account_ids:
            for v1 in self.ec_id_account_ids:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_instance_id is not None:
            result['BillInstanceId'] = self.bill_instance_id

        if self.billing_commodity_code is not None:
            result['BillingCommodityCode'] = self.billing_commodity_code

        if self.billing_end_time is not None:
            result['BillingEndTime'] = self.billing_end_time

        if self.billing_start_time is not None:
            result['BillingStartTime'] = self.billing_start_time

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k1 in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k1.to_map() if k1 else None)

        if self.group is not None:
            result['Group'] = self.group

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.relation_account_ids is not None:
            result['RelationAccountIds'] = self.relation_account_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillInstanceId') is not None:
            self.bill_instance_id = m.get('BillInstanceId')

        if m.get('BillingCommodityCode') is not None:
            self.billing_commodity_code = m.get('BillingCommodityCode')

        if m.get('BillingEndTime') is not None:
            self.billing_end_time = m.get('BillingEndTime')

        if m.get('BillingStartTime') is not None:
            self.billing_start_time = m.get('BillingStartTime')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k1 in m.get('EcIdAccountIds'):
                temp_model = main_models.DescribeDeductLogsRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k1))

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RelationAccountIds') is not None:
            self.relation_account_ids = m.get('RelationAccountIds')

        return self

class DescribeDeductLogsRequestEcIdAccountIds(DaraModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        # The list of accounts to access. If this parameter is empty, all accounts under the current entity ID are selected.
        self.account_ids = account_ids
        # The enterprise entity ID.
        # 
        # This parameter is required.
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids

        if self.ec_id is not None:
            result['EcId'] = self.ec_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')

        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')

        return self

