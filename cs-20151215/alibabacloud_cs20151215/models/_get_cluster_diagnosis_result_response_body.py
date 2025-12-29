# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetClusterDiagnosisResultResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        created: str = None,
        diagnosis_id: str = None,
        finished: str = None,
        message: str = None,
        result: str = None,
        status: int = None,
        target: str = None,
        type: str = None,
    ):
        # The code that indicates the diagnostic result. Valid values:
        # 
        # *   0: the diagnostic is completed.
        # *   1: the diagnostic failed.
        self.code = code
        # The time when the diagnostic is initiated.
        self.created = created
        # The diagnostic ID.
        self.diagnosis_id = diagnosis_id
        # The time when the diagnostic is completed.
        self.finished = finished
        # The diagnostic status information.
        self.message = message
        # The diagnostic result.
        self.result = result
        # The status of the diagnostic. Valid values:
        # 
        # *   0: The diagnostic is created.
        # *   1: The diagnostic is running.
        # *   2: The diagnostic is completed.
        self.status = status
        # The diagnostic object.
        self.target = target
        # The type of the diagnostic.
        # 
        # Valid values:
        # 
        # *   node
        # *   ingress
        # *   cluster
        # *   memory
        # *   pod
        # *   service
        # *   network
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.created is not None:
            result['created'] = self.created

        if self.diagnosis_id is not None:
            result['diagnosis_id'] = self.diagnosis_id

        if self.finished is not None:
            result['finished'] = self.finished

        if self.message is not None:
            result['message'] = self.message

        if self.result is not None:
            result['result'] = self.result

        if self.status is not None:
            result['status'] = self.status

        if self.target is not None:
            result['target'] = self.target

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('diagnosis_id') is not None:
            self.diagnosis_id = m.get('diagnosis_id')

        if m.get('finished') is not None:
            self.finished = m.get('finished')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('target') is not None:
            self.target = m.get('target')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

