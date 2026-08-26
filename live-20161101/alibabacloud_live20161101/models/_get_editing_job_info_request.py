# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEditingJobInfoRequest(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        show_id: str = None,
    ):
        # The production studio ID.
        # 
        # - If you created the production studio by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, check the CasterId parameter in the response.
        # 
        # - If you created the production studio in the ApsaraVideo Live console, navigate to **ApsaraVideo Live console** > **Production Studios** > **Cloud Production Studio** to view the ID.
        # 
        # > - The name of the production studio in the production studio list on the Cloud Production Studio page is the production studio ID.
        # > - CasterId must be a production studio with NormType=6 (playlist mode). Using a production studio with other NormType values (such as 1 or 3) returns InvalidShowList.NotFound. You can filter by NormType=6 in the DescribeCasters response.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The ID of the show to query.
        # >You can obtain the ShowId value from the response of the [AddShowIntoShowList](https://help.aliyun.com/document_detail/370861.html) operation.
        self.show_id = show_id

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

        return self

