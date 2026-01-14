# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetZookeeperDataImportUrlRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        content_type: str = None,
        instance_id: str = None,
    ):
        # RestResult
        self.accept_language = accept_language
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.content_type = content_type
        # The type of the file.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

