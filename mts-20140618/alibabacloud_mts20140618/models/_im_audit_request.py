# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImAuditRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        contents: str = None,
        images: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scenes: str = None,
    ):
        # The business type. By default, the public business type is used.
        self.biz_type = biz_type
        # The custom text entries. You can specify up to 5 text entries. The value must be a JSON array. You must specify at least one of the Images and Contents parameters.
        self.contents = contents
        # The image URLs. You can specify up to 5 image URLs. The value must be a JSON array. To view the URLs of the images, you can log on to the **ApsaraVideo Media Processing (MPS) console** and choose **Media Management** > **Media List** in the left-side navigation pane. You must set at least one of the Images and Contents parameters. The image to be moderated must meet the following limits. Otherwise, the moderation task may fail.
        # 
        # *   The image size cannot exceed 20 MB, the height or width of the image cannot exceed 30,000 pixels, and the image cannot exceed 0.25 billion pixels.
        # *   We recommend that you upload images of at least 256 × 256 pixels to ensure required moderation result.
        self.images = images
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The moderation scenarios. Separate multiple scenarios with commas (,). For example, if you specify {"porn","terrorism"} for this parameter, both pornographic content detection and terrorist content detection are performed on the images and text. Valid values:
        # 
        # *   porn: pornography
        # *   terrorism: terrorist content
        # *   ad: ad violation
        # *   qrcode: QR code
        # *   live: undesirable scene
        # *   logo: special logo
        # *   antispam: text anti-spam (valid only for text)
        # 
        # This parameter is required.
        self.scenes = scenes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.contents is not None:
            result['Contents'] = self.contents

        if self.images is not None:
            result['Images'] = self.images

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scenes is not None:
            result['Scenes'] = self.scenes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('Contents') is not None:
            self.contents = m.get('Contents')

        if m.get('Images') is not None:
            self.images = m.get('Images')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Scenes') is not None:
            self.scenes = m.get('Scenes')

        return self

