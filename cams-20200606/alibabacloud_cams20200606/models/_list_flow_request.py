# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class ListFlowRequest(DaraModel):
    def __init__(
        self,
        cust_space_id: str = None,
        flow_name: str = None,
        owner_id: int = None,
        page: main_models.ListFlowRequestPage = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.cust_space_id = cust_space_id
        self.flow_name = flow_name
        self.owner_id = owner_id
        self.page = page
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page is not None:
            result['Page'] = self.page.to_map()

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Page') is not None:
            temp_model = main_models.ListFlowRequestPage()
            self.page = temp_model.from_map(m.get('Page'))

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

class ListFlowRequestPage(DaraModel):
    def __init__(
        self,
        index: int = None,
        size: int = None,
    ):
        self.index = index
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

