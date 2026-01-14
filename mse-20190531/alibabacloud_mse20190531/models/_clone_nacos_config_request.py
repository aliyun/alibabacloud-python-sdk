# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloneNacosConfigRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        data_ids: str = None,
        ids: str = None,
        instance_id: str = None,
        origin_namespace_id: str = None,
        policy: str = None,
        target_namespace_id: str = None,
    ):
        # Language type of the returned message:
        # 
        # - zh: Chinese
        # - en: English
        self.accept_language = accept_language
        # Configuration items to be cloned, in the format of dataId+group, with multiple items separated by commas.
        self.data_ids = data_ids
        # List of configuration IDs.
        self.ids = ids
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Source namespace ID.
        self.origin_namespace_id = origin_namespace_id
        # The strategy used when a write conflict occurs.
        # 
        # - ABORT
        # - SKIP
        # - OVERWRITE
        # 
        # This parameter is required.
        self.policy = policy
        # Target namespace ID.
        self.target_namespace_id = target_namespace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.data_ids is not None:
            result['DataIds'] = self.data_ids

        if self.ids is not None:
            result['Ids'] = self.ids

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.origin_namespace_id is not None:
            result['OriginNamespaceId'] = self.origin_namespace_id

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.target_namespace_id is not None:
            result['TargetNamespaceId'] = self.target_namespace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('DataIds') is not None:
            self.data_ids = m.get('DataIds')

        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OriginNamespaceId') is not None:
            self.origin_namespace_id = m.get('OriginNamespaceId')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('TargetNamespaceId') is not None:
            self.target_namespace_id = m.get('TargetNamespaceId')

        return self

