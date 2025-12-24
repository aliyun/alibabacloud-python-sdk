# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CopyCasterRequest(DaraModel):
    def __init__(
        self,
        caster_name: str = None,
        client_token: str = None,
        owner_id: int = None,
        region_id: str = None,
        src_caster_id: str = None,
    ):
        # The name of the new production studio.
        # 
        # This parameter is required.
        self.caster_name = caster_name
        # The user-generated request token. This token is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # This parameter is required.
        self.client_token = client_token
        self.owner_id = owner_id
        self.region_id = region_id
        # The ID of the original production studio.
        # 
        # *   If the production studio was created by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, check the value of the response parameter CasterId to obtain the ID.
        # *   If the production studio was created by using the ApsaraVideo Live console, obtain the ID on the **Production Studio Management** page. To go to the page, log on to the **ApsaraVideo Live console** and click **Production Studios** in the left-side navigation pane.
        # 
        # >  You can find the ID of the production studio in the Instance ID/Name column.
        # 
        # This parameter is required.
        self.src_caster_id = src_caster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caster_name is not None:
            result['CasterName'] = self.caster_name

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.src_caster_id is not None:
            result['SrcCasterId'] = self.src_caster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterName') is not None:
            self.caster_name = m.get('CasterName')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SrcCasterId') is not None:
            self.src_caster_id = m.get('SrcCasterId')

        return self

