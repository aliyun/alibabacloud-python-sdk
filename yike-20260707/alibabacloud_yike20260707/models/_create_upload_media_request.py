# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUploadMediaRequest(DaraModel):
    def __init__(
        self,
        credential_type: str = None,
        entity_id: str = None,
        file_info: str = None,
        media_id: str = None,
        media_meta_data: str = None,
        overwrite: bool = None,
        project_id: str = None,
        storage_location: str = None,
        user_data: str = None,
    ):
        # The type of the upload credential. Valid values:
        # - `STS_TOKEN`: the default value. Direct upload by using the OSS SDK.
        # - `POST_POLICY`: form-based upload.
        # - `PRESIGNED_URL`: pre-signed PUT URL.
        # - `UPLOAD_TICKET`: ticket mode. A real credential is issued only when the ticket is exchanged.
        self.credential_type = credential_type
        # The entity ID. The default value is AiSaasMediaAsset. You can ignore this parameter in common calls.
        self.entity_id = entity_id
        # The file information, which is a JSON string. This parameter is required when you create a media asset. The **Type** field is required and can be set to video, audio, or image. The **Name** (file name), **Ext** (file name extension without the period), and **Size** (file size in bytes) fields are optional. This parameter can be omitted when you overwrite an existing media asset (Overwrite=true). If this parameter is omitted, the original media asset type and source file name extension are used.
        self.file_info = file_info
        # The ID of the existing media asset. This parameter is required when Overwrite is set to true (overwrite mode). If CredentialType is set to UPLOAD_TICKET, this parameter indicates a ticket exchange. This parameter is not required in other credential modes.
        self.media_id = media_id
        # The metadata of the media asset, which is a JSON string. This parameter is required when you create a media asset. It can contain the following fields: **Title** (the title; if not specified, FileInfo.Name is used), **Description**, **CateId** (the category ID), **Tags** (comma-separated tags), **BusinessType** (falls back to general if an invalid value is provided), **CoverURL**, **DynamicMetaData** (a JSON string, such as ProductionId), **ReferenceId** (the external reference ID), and **RegisterConfig** (an object that contains SearchLibName to specify the search library). This parameter can be omitted when you overwrite an existing media asset.
        self.media_meta_data = media_meta_data
        # Specifies whether to overwrite the existing media asset. Default value: false. If this parameter is set to true, you must specify MediaId. The original media asset is reset (old files, snapshots, and analysis results are cleared, and the status is set to uploading), and a new credential is issued as if it were the first upload.
        self.overwrite = overwrite
        # The project ID. This parameter has the highest priority and is written to dynamicMetaData.ProductionId, overwriting the value with the same name in DynamicMetaData. It is automatically paired with the default folder `fd__default`. This parameter is supported only by the default entity. If you specify this parameter for a non-default entity, an `InvalidParameter` error is returned. If this parameter is not specified, `ProductionId` is obtained from the existing fallback chain.
        self.project_id = project_id
        # The specified storage location. The format is `bucket.endpoint`. If this parameter is not specified, the default bucket selection policy is used.
        self.storage_location = storage_location
        # The custom user data, which is a JSON string.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.file_info is not None:
            result['FileInfo'] = self.file_info

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_meta_data is not None:
            result['MediaMetaData'] = self.media_meta_data

        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('FileInfo') is not None:
            self.file_info = m.get('FileInfo')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaMetaData') is not None:
            self.media_meta_data = m.get('MediaMetaData')

        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

