# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_yike20260707 import models as main_models
from darabonba.model import DaraModel

class CreateUploadMediaResponseBody(DaraModel):
    def __init__(
        self,
        file_url: str = None,
        media_id: str = None,
        object_key: str = None,
        request_id: str = None,
        storage_location: str = None,
        ticket_expiration: str = None,
        upload_credentials: main_models.CreateUploadMediaResponseBodyUploadCredentials = None,
        upload_ticket: str = None,
    ):
        # The unsigned OSS URL of the file. The format is `oss://bucket/objectKey`.
        self.file_url = file_url
        # The media asset ID.
        self.media_id = media_id
        # The OSS object key. The format is `yike-v1/uid segment-ws segment/date/hour/type/mediaId+random string+source suffix.file name extension`.
        self.object_key = object_key
        # The request ID.
        self.request_id = request_id
        # The storage location identifier. The format is `bucket.endpoint`.
        self.storage_location = storage_location
        # The expiration time of the ticket. The time is in UTC and follows the ISO 8601 standard. This field is returned when UPLOAD_TICKET is used.
        self.ticket_expiration = ticket_expiration
        # The upload credentials. Some fields may be empty depending on the `CredentialType`.
        self.upload_credentials = upload_credentials
        # The upload ticket. This field is returned when UPLOAD_TICKET is used. The ticket is a 27-character string in the format of UT1+region code+random string+check digit. A real credential is issued based on this ticket during a ticket exchange.
        self.upload_ticket = upload_ticket

    def validate(self):
        if self.upload_credentials:
            self.upload_credentials.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_url is not None:
            result['FileURL'] = self.file_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.object_key is not None:
            result['ObjectKey'] = self.object_key

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

        if self.ticket_expiration is not None:
            result['TicketExpiration'] = self.ticket_expiration

        if self.upload_credentials is not None:
            result['UploadCredentials'] = self.upload_credentials.to_map()

        if self.upload_ticket is not None:
            result['UploadTicket'] = self.upload_ticket

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        if m.get('TicketExpiration') is not None:
            self.ticket_expiration = m.get('TicketExpiration')

        if m.get('UploadCredentials') is not None:
            temp_model = main_models.CreateUploadMediaResponseBodyUploadCredentials()
            self.upload_credentials = temp_model.from_map(m.get('UploadCredentials'))

        if m.get('UploadTicket') is not None:
            self.upload_ticket = m.get('UploadTicket')

        return self

class CreateUploadMediaResponseBodyUploadCredentials(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        bucket: str = None,
        expiration: str = None,
        policy: str = None,
        post_access_key_id: str = None,
        post_endpoint: str = None,
        region: str = None,
        security_token: str = None,
        signature: str = None,
        signed_url: str = None,
    ):
        # The temporary STS `AccessKey ID`. This field is returned when `STS_TOKEN` is used.
        self.access_key_id = access_key_id
        # The temporary STS AccessKey secret. This field is returned when STS_TOKEN is used.
        self.access_key_secret = access_key_secret
        # The OSS bucket. This field is returned when STS_TOKEN, POST_POLICY, or PRESIGNED_URL is used.
        self.bucket = bucket
        # The expiration time of the credential. The time is in UTC and follows the ISO 8601 standard.
        self.expiration = expiration
        # The Base64-encoded PostObject policy. This field is returned when POST_POLICY is used.
        self.policy = policy
        # The AccessKey ID used for the signature. This field is returned when POST_POLICY is used.
        self.post_access_key_id = post_access_key_id
        # The target endpoint for the POST request. This field is returned when POST_POLICY is used.
        self.post_endpoint = post_endpoint
        # The OSS region. This field is returned in all three credential modes.
        self.region = region
        # The STS security token. This field is returned when STS_TOKEN is used.
        self.security_token = security_token
        # The PostObject signature. This field is returned when POST_POLICY is used.
        self.signature = signature
        # The pre-signed PUT URL. This field is returned when PRESIGNED_URL is used.
        self.signed_url = signed_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id

        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret

        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.expiration is not None:
            result['Expiration'] = self.expiration

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.post_access_key_id is not None:
            result['PostAccessKeyId'] = self.post_access_key_id

        if self.post_endpoint is not None:
            result['PostEndpoint'] = self.post_endpoint

        if self.region is not None:
            result['Region'] = self.region

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.signature is not None:
            result['Signature'] = self.signature

        if self.signed_url is not None:
            result['SignedUrl'] = self.signed_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')

        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')

        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('PostAccessKeyId') is not None:
            self.post_access_key_id = m.get('PostAccessKeyId')

        if m.get('PostEndpoint') is not None:
            self.post_endpoint = m.get('PostEndpoint')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        if m.get('SignedUrl') is not None:
            self.signed_url = m.get('SignedUrl')

        return self

