# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPreSignedUrlForObjectResult(DaraModel):
    def __init__(
        self,
        jar_url: str = None,
        pre_signed_url: str = None,
    ):
        self.jar_url = jar_url
        self.pre_signed_url = pre_signed_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.jar_url is not None:
            result['jarUrl'] = self.jar_url

        if self.pre_signed_url is not None:
            result['preSignedUrl'] = self.pre_signed_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jarUrl') is not None:
            self.jar_url = m.get('jarUrl')

        if m.get('preSignedUrl') is not None:
            self.pre_signed_url = m.get('preSignedUrl')

        return self

