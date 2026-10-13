# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PublishProductRequest(DaraModel):
    def __init__(
        self,
        portal_id: str = None,
    ):
        # The ID of the HiMarket portal to which the API product is published. This parameter specifies the target portal for the publication. You can query the publication record by portal dimension by calling ListPortalPublications. This ID also appears in the publication record details and is paired with portalName.
        self.portal_id = portal_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.portal_id is not None:
            result['portalId'] = self.portal_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('portalId') is not None:
            self.portal_id = m.get('portalId')

        return self

