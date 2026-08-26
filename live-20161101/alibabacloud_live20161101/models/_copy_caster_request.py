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
        # A client-generated token that ensures the idempotence of the request.
        # 
        # Generate a unique value for this parameter for each request. The token can contain a maximum of 64 ASCII characters.
        # 
        # This parameter is required.
        self.client_token = client_token
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The ID of the production studio to copy.
        # 
        # - If you created the production studio by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, use the CasterId value that is returned.
        # 
        # - If you created the production studio in the ApsaraVideo Live console, go to **ApsaraVideo Live console** > **Production Studio** > **Cloud Production Studio** to view the production studio name.
        # 
        # > The name of a production studio on the Cloud Production Studio page is its production studio ID.
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

