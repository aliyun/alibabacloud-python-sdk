# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetIdpMetadataRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        idp_metadata: str = None,
        office_site_id: str = None,
        region_id: str = None,
    ):
        # The office network ID, which has the same meaning as `OfficeSiteId`. We recommend that you stop using `DirectoryId` and use `OfficeSiteId` instead. You can specify only one of `DirectoryId` and `OfficeSiteId`, not both.
        self.directory_id = directory_id
        # The metadata of the identity provider (IdP).
        # 
        # This parameter is required.
        self.idp_metadata = idp_metadata
        # The office network ID.
        self.office_site_id = office_site_id
        # The region ID. You can call [DescribeRegions](~~DescribeRegions~~) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.idp_metadata is not None:
            result['IdpMetadata'] = self.idp_metadata

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('IdpMetadata') is not None:
            self.idp_metadata = m.get('IdpMetadata')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

