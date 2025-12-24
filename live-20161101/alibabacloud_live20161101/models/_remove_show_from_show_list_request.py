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
        # *   If the production studio was created by calling the [CreateCaster](https://help.aliyun.com/document_detail/69338.html) operation, check the value of the response parameter CasterId to obtain the ID.
        # *   If the production studio was created by using the ApsaraVideo Live console, obtain the ID on the **Production Studio Management** page. To go to the page, log on to the **ApsaraVideo Live console** and click **Production Studios** in the left-side navigation pane.
        # 
        # >  You can find the ID of the production studio in the Instance ID/Name column.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        self.owner_id = owner_id
        self.region_id = region_id
        # The ID of the episode.
        # 
        # >  You can obtain the ID by checking the value of the response parameter ShowId of the [AddShowIntoShowList](https://help.aliyun.com/document_detail/370861.html) operation.
        self.show_id = show_id
        # Specifies whether to remove multiple episodes at a time. Valid values:
        # 
        # *   true: removes multiple episodes at a time.
        # *   false: removes a single episode.
        # 
        # >  If you do not configure this parameter or this parameter is left empty, a single episode is to be removed.
        self.is_batch_mode = is_batch_mode
        # The IDs of episodes that you want to remove.
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

