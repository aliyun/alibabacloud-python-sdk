# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ShareOptions(DaraModel):
    def __init__(
        self,
        catalog_size_limit: int = None,
        receiver_size_limit: int = None,
        share_resource_size_limit: int = None,
        share_size_limit: int = None,
    ):
        self.catalog_size_limit = catalog_size_limit
        self.receiver_size_limit = receiver_size_limit
        self.share_resource_size_limit = share_resource_size_limit
        self.share_size_limit = share_size_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_size_limit is not None:
            result['catalogSizeLimit'] = self.catalog_size_limit

        if self.receiver_size_limit is not None:
            result['receiverSizeLimit'] = self.receiver_size_limit

        if self.share_resource_size_limit is not None:
            result['shareResourceSizeLimit'] = self.share_resource_size_limit

        if self.share_size_limit is not None:
            result['shareSizeLimit'] = self.share_size_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('catalogSizeLimit') is not None:
            self.catalog_size_limit = m.get('catalogSizeLimit')

        if m.get('receiverSizeLimit') is not None:
            self.receiver_size_limit = m.get('receiverSizeLimit')

        if m.get('shareResourceSizeLimit') is not None:
            self.share_resource_size_limit = m.get('shareResourceSizeLimit')

        if m.get('shareSizeLimit') is not None:
            self.share_size_limit = m.get('shareSizeLimit')

        return self

