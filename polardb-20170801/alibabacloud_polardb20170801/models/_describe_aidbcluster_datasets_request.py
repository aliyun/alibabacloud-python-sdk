# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAIDBClusterDatasetsRequest(DaraModel):
    def __init__(
        self,
        continuation_token: str = None,
        dbcluster_id: str = None,
        dataset_id: str = None,
        dataset_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        train_mode: str = None,
    ):
        # The token used to retrieve the next page of results. This value is obtained from the response of a previous request. For the first request, leave this parameter empty.
        self.continuation_token = continuation_token
        # The ID of the PolarDB cluster for AI model services.
        self.dbcluster_id = dbcluster_id
        # The dataset ID.
        self.dataset_id = dataset_id
        # The type of the dataset. Valid values:
        # 
        # - **train**: The training set.
        # 
        # - **eval**: The evaluation set.
        self.dataset_type = dataset_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number to return. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: **30**, **50**, and **100**.
        # 
        # Default value: **30**.
        self.page_size = page_size
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The training mode. Valid values:
        # 
        # - **sft**: supervised fine-tuning.
        # 
        # - **grpo**: reinforcement learning.
        # 
        # - **text**: text generation.
        self.train_mode = train_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.continuation_token is not None:
            result['ContinuationToken'] = self.continuation_token

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.dataset_type is not None:
            result['DatasetType'] = self.dataset_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.train_mode is not None:
            result['TrainMode'] = self.train_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContinuationToken') is not None:
            self.continuation_token = m.get('ContinuationToken')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('DatasetType') is not None:
            self.dataset_type = m.get('DatasetType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TrainMode') is not None:
            self.train_mode = m.get('TrainMode')

        return self

