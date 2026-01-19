# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAggregatorShrinkRequest(DaraModel):
    def __init__(
        self,
        aggregator_accounts_shrink: str = None,
        aggregator_id: str = None,
        aggregator_name: str = None,
        client_token: str = None,
        description: str = None,
        folder_id: str = None,
        tag_shrink: str = None,
    ):
        # The members in the account group.
        # 
        # >  When you modify the configurations of an account group, this parameter can be left empty. In this case, the member list is not updated. If you want to update the member list, you must configure both the `AccountId` and `AccountType` parameters.
        self.aggregator_accounts_shrink = aggregator_accounts_shrink
        # The ID of the account group.
        # 
        # For more information about how to obtain the ID of an account group, see [ListAggregators](https://help.aliyun.com/document_detail/255797.html).
        # 
        # This parameter is required.
        self.aggregator_id = aggregator_id
        # The name of the account group.
        # 
        # For more information about how to obtain the name of an account group, see [ListAggregators](https://help.aliyun.com/document_detail/255797.html).
        self.aggregator_name = aggregator_name
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The description of the account group.
        # 
        # For more information about how to obtain the description of an account group, see [ListAggregators](https://help.aliyun.com/document_detail/255797.html).
        self.description = description
        # The folder ID. Separate multiple folder IDs with commas (,).
        self.folder_id = folder_id
        # The tags of the resource.
        # 
        # You can add up to 20 tags to a resource.
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregator_accounts_shrink is not None:
            result['AggregatorAccounts'] = self.aggregator_accounts_shrink

        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

        if self.aggregator_name is not None:
            result['AggregatorName'] = self.aggregator_name

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorAccounts') is not None:
            self.aggregator_accounts_shrink = m.get('AggregatorAccounts')

        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('AggregatorName') is not None:
            self.aggregator_name = m.get('AggregatorName')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        return self

