# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMultimodeCmsUrlResponseBody(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        multimod_cms_url: str = None,
        request_id: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The CloudMonitor URL.
        self.multimod_cms_url = multimod_cms_url
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.multimod_cms_url is not None:
            result['MultimodCmsUrl'] = self.multimod_cms_url

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('MultimodCmsUrl') is not None:
            self.multimod_cms_url = m.get('MultimodCmsUrl')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

