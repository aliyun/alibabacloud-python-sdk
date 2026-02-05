# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportScriptRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        nlu_engine: str = None,
        signature_url: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.nlu_engine = nlu_engine
        # This parameter is required.
        self.signature_url = signature_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.nlu_engine is not None:
            result['NluEngine'] = self.nlu_engine

        if self.signature_url is not None:
            result['SignatureUrl'] = self.signature_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NluEngine') is not None:
            self.nlu_engine = m.get('NluEngine')

        if m.get('SignatureUrl') is not None:
            self.signature_url = m.get('SignatureUrl')

        return self

