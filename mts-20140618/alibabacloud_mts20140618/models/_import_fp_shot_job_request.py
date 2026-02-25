# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportFpShotJobRequest(DaraModel):
    def __init__(
        self,
        fp_dbid: str = None,
        fp_import_config: str = None,
        input: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pipeline_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        user_data: str = None,
    ):
        # The ID of the text fingerprint library to which the text file is imported. You can specify only one job of importing text files to a text fingerprint library at a time. You can obtain the library ID from the response parameters of the [CreateFpShotDB](https://help.aliyun.com/document_detail/170149.html) operation.
        # 
        # This parameter is required.
        self.fp_dbid = fp_dbid
        # The job configurations. The value must be a JSON object. Example: `{"SaveType":"onlysave"}`. The `SaveType` field indicates the storage type. Valid values of the SaveType field:
        # 
        # *   **save**: The fingerprints of the text file are saved to the text fingerprint library only if the text file is not duplicated with content in the text fingerprint library.
        # *   **onlysave**: The fingerprints of the text file are saved to the text fingerprint library.
        # 
        # This parameter is required.
        self.fp_import_config = fp_import_config
        # The Object Storage Service (OSS) URL of the text file to be imported to the text fingerprint library. The value must be a JSON object. Example: {"Bucket":"example-bucket","Location":"oss-cn-shanghai","Object":"example.flv"}.
        # 
        # > The OSS bucket must reside in the same region as your MPS service.
        # 
        # This parameter is required.
        self.input = input
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the ApsaraVideo Media Processing (MPS) queue. To view the ID of the MPS queue, perform the following steps: Log on to the **MPS console**. In the left-side navigation pane, choose **Global Settings** > **Pipelines**. The MPS queue is associated with a specified Message Service (MNS) topic. You can submit jobs for different services to different MPS queues. If you do not specify this parameter, the job is submitted to the default MPS queue and no MNS topic is associated with the MPS queue.
        self.pipeline_id = pipeline_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The user-defined data. The value can contain letters, digits, and special characters. The value can be up to 128 bytes in length.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fp_dbid is not None:
            result['FpDBId'] = self.fp_dbid

        if self.fp_import_config is not None:
            result['FpImportConfig'] = self.fp_import_config

        if self.input is not None:
            result['Input'] = self.input

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FpDBId') is not None:
            self.fp_dbid = m.get('FpDBId')

        if m.get('FpImportConfig') is not None:
            self.fp_import_config = m.get('FpImportConfig')

        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

