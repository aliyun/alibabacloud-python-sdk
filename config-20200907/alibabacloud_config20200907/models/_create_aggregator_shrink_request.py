# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAggregatorShrinkRequest(DaraModel):
    def __init__(
        self,
        aggregator_accounts_shrink: str = None,
        aggregator_name: str = None,
        aggregator_type: str = None,
        client_token: str = None,
        description: str = None,
        folder_id: str = None,
        tag_shrink: str = None,
    ):
        # The member accounts of the account group.
        # 
        # > - If you set `AggregatorType` to \\`RD, you can leave this parameter empty. This indicates that all members in the resource directory are added to the global account group.
        # >
        # > - If you set `AggregatorType` to `FOLDER`, you can leave this parameter empty. This indicates that all members in a specific folder in the resource directory are added to the folder account group.
        self.aggregator_accounts_shrink = aggregator_accounts_shrink
        # The name of the account group.
        # 
        # This parameter is required.
        self.aggregator_name = aggregator_name
        # The type of the account group. Valid values:
        # 
        # - RD: global account group.
        # 
        # - FOLDER: folder account group. You must also set the `FolderId` parameter. For more information about how to obtain a folder ID, see [ListAccounts](https://help.aliyun.com/document_detail/160016.html).
        # 
        # - CUSTOM (default): custom account group. You must also set the `AccountId` and `AccountType` parameters for `AggregatorAccounts`.
        self.aggregator_type = aggregator_type
        # A client token that is used to ensure the idempotence of the request. You must make sure that the token is unique for different requests. The `ClientToken` parameter can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The description of the account group.
        self.description = description
        # The ID of the attached folder. You can specify multiple folder IDs. Separate the IDs with commas (,).
        # 
        # This parameter is required if you set `AggregatorType` to `FOLDER`.
        self.folder_id = folder_id
        # The tags of the resource.
        # 
        # You can attach a maximum of 20 tags.
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

        if self.aggregator_name is not None:
            result['AggregatorName'] = self.aggregator_name

        if self.aggregator_type is not None:
            result['AggregatorType'] = self.aggregator_type

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

        if m.get('AggregatorName') is not None:
            self.aggregator_name = m.get('AggregatorName')

        if m.get('AggregatorType') is not None:
            self.aggregator_type = m.get('AggregatorType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        return self

