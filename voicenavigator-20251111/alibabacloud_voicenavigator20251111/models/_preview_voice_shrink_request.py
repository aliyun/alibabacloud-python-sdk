# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PreviewVoiceShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        model: str = None,
        nls_access_type: str = None,
        nls_engine: str = None,
        params_shrink: str = None,
        text: str = None,
        voice: str = None,
    ):
        self.instance_id = instance_id
        self.model = model
        self.nls_access_type = nls_access_type
        self.nls_engine = nls_engine
        self.params_shrink = params_shrink
        self.text = text
        self.voice = voice

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

        if self.params_shrink is not None:
            result['Params'] = self.params_shrink

        if self.text is not None:
            result['Text'] = self.text

        if self.voice is not None:
            result['Voice'] = self.voice

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

        if m.get('Params') is not None:
            self.params_shrink = m.get('Params')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Voice') is not None:
            self.voice = m.get('Voice')

        return self

