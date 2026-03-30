# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class GetOIDCProviderResponseBody(DaraModel):
    def __init__(
        self,
        oidcprovider: main_models.GetOIDCProviderResponseBodyOIDCProvider = None,
        request_id: str = None,
    ):
        # The information about the OIDC IdP.
        self.oidcprovider = oidcprovider
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.oidcprovider:
            self.oidcprovider.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oidcprovider is not None:
            result['OIDCProvider'] = self.oidcprovider.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OIDCProvider') is not None:
            temp_model = main_models.GetOIDCProviderResponseBodyOIDCProvider()
            self.oidcprovider = temp_model.from_map(m.get('OIDCProvider'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetOIDCProviderResponseBodyOIDCProvider(DaraModel):
    def __init__(
        self,
        arn: str = None,
        client_ids: str = None,
        create_date: str = None,
        description: str = None,
        fingerprints: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        issuance_limit_time: int = None,
        issuer_url: str = None,
        oidcprovider_name: str = None,
        update_date: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the OIDC IdP.
        self.arn = arn
        # The ID of the client. If multiple client IDs are returned, the client IDs are separated by commas (,).
        self.client_ids = client_ids
        # The time when the OIDC IdP was created. The time is displayed in UTC.
        self.create_date = create_date
        # The description of the OIDC IdP.
        self.description = description
        # The fingerprint of the HTTPS certificate. If multiple fingerprints are returned, the fingerprints are separated by commas (,).
        self.fingerprints = fingerprints
        # The timestamp when the OIDC IdP was created.
        self.gmt_create = gmt_create
        # The timestamp when the OIDC IdP was modified.
        self.gmt_modified = gmt_modified
        # The earliest time when an external IdP can issue an ID token. If the value of the iat field in the ID token is later than the current time, the request is rejected. Unit: hours. Valid values: 1 to 168.
        self.issuance_limit_time = issuance_limit_time
        # The URL of the issuer.
        self.issuer_url = issuer_url
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name
        # The time when the OIDC IdP was modified. The time is displayed in UTC.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.description is not None:
            result['Description'] = self.description

        if self.fingerprints is not None:
            result['Fingerprints'] = self.fingerprints

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.issuance_limit_time is not None:
            result['IssuanceLimitTime'] = self.issuance_limit_time

        if self.issuer_url is not None:
            result['IssuerUrl'] = self.issuer_url

        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name

        if self.update_date is not None:
            result['UpdateDate'] = self.update_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Fingerprints') is not None:
            self.fingerprints = m.get('Fingerprints')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('IssuanceLimitTime') is not None:
            self.issuance_limit_time = m.get('IssuanceLimitTime')

        if m.get('IssuerUrl') is not None:
            self.issuer_url = m.get('IssuerUrl')

        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        return self

