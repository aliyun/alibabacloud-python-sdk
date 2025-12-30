# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitVideoTranslationJobRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        editing_config: str = None,
        input_config: str = None,
        output_config: str = None,
        signature: str = None,
        signature_mehtod: str = None,
        signature_nonce: str = None,
        signature_type: str = None,
        signature_version: str = None,
        title: str = None,
        user_data: str = None,
    ):
        # *   The client token.
        self.client_token = client_token
        # *   The job description.
        self.description = description
        # *   The configuration parameters of the video translation job.
        # *   The value must be in the JSON format.
        self.editing_config = editing_config
        # *   The input parameters of the video translation job.
        # *   A video translation job takes a video or subtitle file as the input.
        # *   The value must be in the JSON format.
        self.input_config = input_config
        # *   The output parameters of the video translation job.
        # *   A video translation job can generate a video or subtitle file as the output.
        self.output_config = output_config
        self.signature = signature
        self.signature_mehtod = signature_mehtod
        self.signature_nonce = signature_nonce
        self.signature_type = signature_type
        self.signature_version = signature_version
        # *   The job title.
        self.title = title
        # *   The user-defined data.
        # *   The data must be in the JSON format, and can be up to 512 characters in length.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.editing_config is not None:
            result['EditingConfig'] = self.editing_config

        if self.input_config is not None:
            result['InputConfig'] = self.input_config

        if self.output_config is not None:
            result['OutputConfig'] = self.output_config

        if self.signature is not None:
            result['Signature'] = self.signature

        if self.signature_mehtod is not None:
            result['SignatureMehtod'] = self.signature_mehtod

        if self.signature_nonce is not None:
            result['SignatureNonce'] = self.signature_nonce

        if self.signature_type is not None:
            result['SignatureType'] = self.signature_type

        if self.signature_version is not None:
            result['SignatureVersion'] = self.signature_version

        if self.title is not None:
            result['Title'] = self.title

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EditingConfig') is not None:
            self.editing_config = m.get('EditingConfig')

        if m.get('InputConfig') is not None:
            self.input_config = m.get('InputConfig')

        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        if m.get('SignatureMehtod') is not None:
            self.signature_mehtod = m.get('SignatureMehtod')

        if m.get('SignatureNonce') is not None:
            self.signature_nonce = m.get('SignatureNonce')

        if m.get('SignatureType') is not None:
            self.signature_type = m.get('SignatureType')

        if m.get('SignatureVersion') is not None:
            self.signature_version = m.get('SignatureVersion')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

