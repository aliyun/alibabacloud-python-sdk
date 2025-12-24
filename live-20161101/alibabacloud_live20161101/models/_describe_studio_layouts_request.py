# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeStudioLayoutsRequest(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        layout_id: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        # The ID of the production studio instance.
        # 
        # *   If you call the [CreateCaster](https://help.aliyun.com/document_detail/69338.html) operation to create a production studio instance, you can obtain the instance ID from the CasterId parameter in the response.
        # *   If you create a production studio instance in the ApsaraVideo Live console, perform the following operations to obtain the instance ID: Log on to the **ApsaraVideo Live console** and click **Production Studios** in the left-side navigation pane. Then, view the instance ID on the **Production Studio Management** page.
        # 
        # >  The value displayed in the Name column for an instance on the Production Studio Management page is the ID of the instance.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The ID of the layout.
        # 
        # You can specify multiple layout IDs and separate them with commas (,). If you leave this parameter empty, all layouts of the production studio are returned.
        # 
        # If you call the [AddStudioLayout](https://help.aliyun.com/document_detail/215388.html) operation to configure a layout for a virtual studio, you can obtain the ID of the layout from the LayoutId parameter in the response.
        self.layout_id = layout_id
        self.owner_id = owner_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

