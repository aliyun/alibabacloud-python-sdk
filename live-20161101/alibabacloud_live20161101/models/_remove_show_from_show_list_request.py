# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RemoveShowFromShowListRequest(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        show_id: str = None,
        is_batch_mode: bool = None,
        show_id_list: List[str] = None,
    ):
        # The ID of the production studio.
        # 
        # - If you created the production studio by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, use the CasterId value that is returned in the response.
        # 
        # - If you created the production studio in the LIVE console, find the production studio name in the LIVE console by choosing **LIVE Console** > **Production Studio** > **Cloud Production Studio**.
        # 
        # > The name of the production studio in the list on the Cloud Production Studio page is the production studio ID.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The show ID.
        # 
        # > Obtain the ShowId from the response of the [AddShowIntoShowList](https://help.aliyun.com/document_detail/2848051.html) operation.
        self.show_id = show_id
        # Specifies whether to delete shows in a batch. Valid values:
        # 
        # - true: Deletes shows in a batch.
        # 
        # - false: Deletes a single show.
        # 
        # > If you do not specify this parameter or leave it empty, a single show is deleted.
        self.is_batch_mode = is_batch_mode
        # The IDs of the shows to delete.
        self.show_id_list = show_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.show_id is not None:
            result['ShowId'] = self.show_id

        if self.is_batch_mode is not None:
            result['isBatchMode'] = self.is_batch_mode

        if self.show_id_list is not None:
            result['showIdList'] = self.show_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ShowId') is not None:
            self.show_id = m.get('ShowId')

        if m.get('isBatchMode') is not None:
            self.is_batch_mode = m.get('isBatchMode')

        if m.get('showIdList') is not None:
            self.show_id_list = m.get('showIdList')

        return self

