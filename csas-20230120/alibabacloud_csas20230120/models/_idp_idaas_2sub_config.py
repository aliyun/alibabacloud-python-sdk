# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IdpIdaas2SubConfig(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        client_id: str = None,
        client_secret: str = None,
        event_aes_key: str = None,
        event_label: str = None,
        instance_id: str = None,
        public_key_endpoint: str = None,
        region: str = None,
        saml_metadata: str = None,
    ):
        self.application_id = application_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.event_aes_key = event_aes_key
        self.event_label = event_label
        self.instance_id = instance_id
        self.public_key_endpoint = public_key_endpoint
        self.region = region
        self.saml_metadata = saml_metadata

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret

        if self.event_aes_key is not None:
            result['EventAesKey'] = self.event_aes_key

        if self.event_label is not None:
            result['EventLabel'] = self.event_label

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.public_key_endpoint is not None:
            result['PublicKeyEndpoint'] = self.public_key_endpoint

        if self.region is not None:
            result['Region'] = self.region

        if self.saml_metadata is not None:
            result['SamlMetadata'] = self.saml_metadata

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')

        if m.get('EventAesKey') is not None:
            self.event_aes_key = m.get('EventAesKey')

        if m.get('EventLabel') is not None:
            self.event_label = m.get('EventLabel')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PublicKeyEndpoint') is not None:
            self.public_key_endpoint = m.get('PublicKeyEndpoint')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SamlMetadata') is not None:
            self.saml_metadata = m.get('SamlMetadata')

        return self

