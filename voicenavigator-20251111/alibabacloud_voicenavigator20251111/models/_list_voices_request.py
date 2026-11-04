# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListVoicesRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        model: str = None,
        nls_access_type: str = None,
        nls_engine: str = None,
        omni_model: bool = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # The model.
        self.model = model
        # The TTS invocation method.
        self.nls_access_type = nls_access_type
        # The TTS engine.
        self.nls_engine = nls_engine
        # Specifies whether the model is an Omni model.
        self.omni_model = omni_model
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.model is not None:
            result['Model'] = self.model

        if self.nls_access_type is not None:
            result['NlsAccessType'] = self.nls_access_type

        if self.nls_engine is not None:
            result['NlsEngine'] = self.nls_engine

        if self.omni_model is not None:
            result['OmniModel'] = self.omni_model

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('NlsAccessType') is not None:
            self.nls_access_type = m.get('NlsAccessType')

        if m.get('NlsEngine') is not None:
            self.nls_engine = m.get('NlsEngine')

        if m.get('OmniModel') is not None:
            self.omni_model = m.get('OmniModel')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

