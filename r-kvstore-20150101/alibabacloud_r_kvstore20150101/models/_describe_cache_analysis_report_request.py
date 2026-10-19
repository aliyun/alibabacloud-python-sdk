# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCacheAnalysisReportRequest(DaraModel):
    def __init__(
        self,
        analysis_type: str = None,
        date: str = None,
        instance_id: str = None,
        node_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_numbers: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # The analysis type. Set the value to **BigKey**.
        # 
        # This parameter is required.
        self.analysis_type = analysis_type
        # The date to query. You can query the offline full key analysis results for one day at a time. The format is <i>yyyy-MM-dd</i>Z (UTC time).
        # 
        # This parameter is required.
        self.date = date
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the child node in a cluster instance.
        # > This parameter is required for cluster instances.
        self.node_id = node_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return.
        # > If the value is greater than the maximum number of pages in the returned result, the returned big key results are empty.
        self.page_numbers = page_numbers
        # The number of entries to return on each page. Valid values: **30**, **50**, and **100**.
        # > Default value: **30**.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis_type is not None:
            result['AnalysisType'] = self.analysis_type

        if self.date is not None:
            result['Date'] = self.date

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_numbers is not None:
            result['PageNumbers'] = self.page_numbers

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnalysisType') is not None:
            self.analysis_type = m.get('AnalysisType')

        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumbers') is not None:
            self.page_numbers = m.get('PageNumbers')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

