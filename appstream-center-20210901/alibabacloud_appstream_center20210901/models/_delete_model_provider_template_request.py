# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteModelProviderTemplateRequest(DaraModel):
    def __init__(
        self,
        provider_template_id: str = None,
    ):
        # This parameter is required.
        self.provider_template_id = provider_template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.provider_template_id is not None:
            result['ProviderTemplateId'] = self.provider_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProviderTemplateId') is not None:
            self.provider_template_id = m.get('ProviderTemplateId')

        return self

