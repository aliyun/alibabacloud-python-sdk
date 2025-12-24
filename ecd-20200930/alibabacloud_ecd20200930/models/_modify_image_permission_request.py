# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyImagePermissionRequest(DaraModel):
    def __init__(
        self,
        add_account: List[int] = None,
        image_id: str = None,
        region_id: str = None,
        remove_account: List[int] = None,
    ):
        # The IDs of Alibaba Cloud accounts to which to share the image that will be created based on the image template. You can specify up to 20 account IDs.
        self.add_account = add_account
        # The IDs of the images.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of Alibaba Cloud account N from which you want to unshare the custom image. Valid values of N: 1 to 10. If the value of N is greater than 10, this parameter is ignored.
        self.remove_account = remove_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_account is not None:
            result['AddAccount'] = self.add_account

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remove_account is not None:
            result['RemoveAccount'] = self.remove_account

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddAccount') is not None:
            self.add_account = m.get('AddAccount')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RemoveAccount') is not None:
            self.remove_account = m.get('RemoveAccount')

        return self

