# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class ListMessageCampaignResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[main_models.ListMessageCampaignResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.total = total

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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

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

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListMessageCampaignResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListMessageCampaignResponseBodyData(DaraModel):
    def __init__(
        self,
        ad_account_id: str = None,
        budget: int = None,
        budget_type: str = None,
        campaign_id: str = None,
        campaign_name: str = None,
        create_time: int = None,
        page_id: str = None,
        status: str = None,
    ):
        self.ad_account_id = ad_account_id
        self.budget = budget
        self.budget_type = budget_type
        self.campaign_id = campaign_id
        self.campaign_name = campaign_name
        self.create_time = create_time
        self.page_id = page_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ad_account_id is not None:
            result['AdAccountId'] = self.ad_account_id

        if self.budget is not None:
            result['Budget'] = self.budget

        if self.budget_type is not None:
            result['BudgetType'] = self.budget_type

        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id

        if self.campaign_name is not None:
            result['CampaignName'] = self.campaign_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.page_id is not None:
            result['PageId'] = self.page_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdAccountId') is not None:
            self.ad_account_id = m.get('AdAccountId')

        if m.get('Budget') is not None:
            self.budget = m.get('Budget')

        if m.get('BudgetType') is not None:
            self.budget_type = m.get('BudgetType')

        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')

        if m.get('CampaignName') is not None:
            self.campaign_name = m.get('CampaignName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('PageId') is not None:
            self.page_id = m.get('PageId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

