# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class ListMessageCampaignRequest(DaraModel):
    def __init__(
        self,
        ad_account_id: str = None,
        campaign_id: str = None,
        campaign_name: str = None,
        cust_space_id: str = None,
        owner_id: int = None,
        page: main_models.ListMessageCampaignRequestPage = None,
        page_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
    ):
        self.ad_account_id = ad_account_id
        self.campaign_id = campaign_id
        self.campaign_name = campaign_name
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        # This parameter is required.
        self.page = page
        # This parameter is required.
        self.page_id = page_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.status = status

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ad_account_id is not None:
            result['AdAccountId'] = self.ad_account_id

        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id

        if self.campaign_name is not None:
            result['CampaignName'] = self.campaign_name

        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page is not None:
            result['Page'] = self.page.to_map()

        if self.page_id is not None:
            result['PageId'] = self.page_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdAccountId') is not None:
            self.ad_account_id = m.get('AdAccountId')

        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')

        if m.get('CampaignName') is not None:
            self.campaign_name = m.get('CampaignName')

        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Page') is not None:
            temp_model = main_models.ListMessageCampaignRequestPage()
            self.page = temp_model.from_map(m.get('Page'))

        if m.get('PageId') is not None:
            self.page_id = m.get('PageId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListMessageCampaignRequestPage(DaraModel):
    def __init__(
        self,
        index: int = None,
        size: int = None,
    ):
        # This parameter is required.
        self.index = index
        # This parameter is required.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index is not None:
            result['Index'] = self.index

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

