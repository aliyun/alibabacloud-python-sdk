# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddImageRequest(DaraModel):
    def __init__(
        self,
        category_id: int = None,
        crop: bool = None,
        custom_content: str = None,
        instance_name: str = None,
        int_attr: int = None,
        int_attr_2: int = None,
        int_attr_3: int = None,
        int_attr_4: int = None,
        pic_content: str = None,
        pic_name: str = None,
        product_id: str = None,
        region: str = None,
        str_attr: str = None,
        str_attr_2: str = None,
        str_attr_3: str = None,
        str_attr_4: str = None,
    ):
        # The image category. For more information, refer to [Category reference](https://help.aliyun.com/document_detail/179184.html).
        # > - For product image search, if you specify a category, the specified category is used. If you do not specify a category, the system predicts the category. The predicted category result can be obtained from the response.
        # <props="china">
        # - For fabric, trademark, generic, furniture, and industrial hardware image search, the system sets the category to 88888888 regardless of whether you specify a category.
        # 
        # - For generic image search, the system sets the category to 88888888 regardless of whether you specify a category.
        self.category_id = category_id
        # Specifies whether to perform subject identification. Default value: true.
        #  - true: The system performs subject identification and searches based on the identified subject. The subject identification result can be obtained from the response.
        # - false: The system does not perform subject identification and searches based on the entire image.
        # 
        # <props="china">For fabric image search, this parameter is ignored. The system searches based on the entire image..
        self.crop = crop
        # The custom content defined by the user. The content can be up to 4,096 characters in length.
        # >This field is returned in query results. For example, you can add a text description of the image.
        self.custom_content = custom_content
        # The name of the Image Search instance. The name can be up to 20 characters in length.
        # If you have purchased an Image Search instance, log on to the [Image Search console](https://imagesearch.console.aliyun.com/) to view the instance name.
        # If you have not purchased an Image Search instance, refer to [Activate the service](https://help.aliyun.com/document_detail/179178.html) and [Create an instance](https://help.aliyun.com/document_detail/66569.html).
        # >The instance name is not the instance ID. Do not confuse the two.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The integer attribute. This attribute can be used to filter query results and is returned in query results.
        self.int_attr = int_attr
        # The integer attribute. This attribute can be used to filter query results and is returned in query results.
        self.int_attr_2 = int_attr_2
        # The integer attribute. This attribute can be used to filter query results and is returned in query results.
        self.int_attr_3 = int_attr_3
        # The integer attribute. This attribute can be used to filter query results and is returned in query results.
        self.int_attr_4 = int_attr_4
        # The image content.
        #  - The image size cannot exceed 4 MB.
        #  - Image formats: PNG, JPG, JPEG, BMP, GIF, WEBP, TIFF, and PPM.
        #  - The transmission wait time cannot exceed 5 seconds.
        # <props="china">
        #  - For product image search, generic image search, furniture image search, and industrial hardware image search, the image width and height must be at least 100 pixels and at most 4,096 pixels.
        #   For trademark image search, the image width and height must be at least 200 pixels and less than 4,096 pixels.
        #  For fabric image search, the image width and height must be at least 448 pixels and at most 4,096 pixels.
        # 
        # <props="intl">
        #  - For product image search and generic image search, the image width and height must be at least 100 pixels and at most 4,096 pixels.
        # 
        # - The image must not contain rotation information.
        # 
        # > - **When calling by using an SDK:**
        #   - If you use a V3 SDK, you do not need to set the PicContent field. The SDK encapsulates this field as PicContentObject and automatically converts it to Base64 encoding. For specific examples, refer to [Java SDK](https://help.aliyun.com/document_detail/179188.html).
        #   - The SDK does not support passing image URLs directly. The V3 SDK provides an alternative method to upload images by URL. For specific examples, refer to [Java SDK](https://help.aliyun.com/document_detail/179188.html).
        # - **When calling by using the Alibaba Cloud OpenAPI platform:**
        #   - If you use the **2019-03-25** version, set the **PicContent** field to the **Base64** encoding of the image.
        #   - If you use the **2020-12-14** version, click to upload the image directly in the **PicContent** field.
        # 
        # This parameter is required.
        self.pic_content = pic_content
        # The image name. The name can be up to 256 characters in length.
        # > - ProductId and PicName uniquely identify an image.
        # - If you add multiple images with the same ProductId and PicName, only the last added image is retained. Previously added images are overwritten.
        # 
        # This parameter is required.
        self.pic_name = pic_name
        # The product ID. The ID can be up to 256 characters in length.
        # 
        # >A product can have multiple images.
        # 
        # This parameter is required.
        self.product_id = product_id
        # The subject region of the image, in the format of `x1,x2,y1,y2`, where `x1,y1` is the upper-left point and `x2,y2` is the lower-right point.
        # > - If you specify Region, the system searches based on the specified Region regardless of the Crop parameter value.
        # <props="china">
        # - For fabric image search, this parameter is ignored. The system searches based on the entire image.
        # 
        # - The Region parameter has no unit. The values are based on the pixel dimensions of the image. If the image is scaled, the Region parameter values must be scaled proportionally.
        self.region = region
        # The string attribute. The attribute can be up to 128 characters in length. This attribute can be used to filter query results and is returned in query results.
        # > Special characters such as \\¥$&% are not supported.
        self.str_attr = str_attr
        # The string attribute. The attribute can be up to 128 characters in length. This attribute can be used to filter query results and is returned in query results.
        # > Special characters such as \\¥$&% are not supported.
        self.str_attr_2 = str_attr_2
        # The string attribute. The attribute can be up to 128 characters in length. This attribute can be used to filter query results and is returned in query results.
        # > Special characters such as \\¥$&% are not supported.
        self.str_attr_3 = str_attr_3
        # The string attribute. The attribute can be up to 128 characters in length. This attribute can be used to filter query results and is returned in query results.
        # > Special characters such as \\¥$&% are not supported.
        self.str_attr_4 = str_attr_4

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.crop is not None:
            result['Crop'] = self.crop

        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr

        if self.int_attr_2 is not None:
            result['IntAttr2'] = self.int_attr_2

        if self.int_attr_3 is not None:
            result['IntAttr3'] = self.int_attr_3

        if self.int_attr_4 is not None:
            result['IntAttr4'] = self.int_attr_4

        if self.pic_content is not None:
            result['PicContent'] = self.pic_content

        if self.pic_name is not None:
            result['PicName'] = self.pic_name

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.region is not None:
            result['Region'] = self.region

        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr

        if self.str_attr_2 is not None:
            result['StrAttr2'] = self.str_attr_2

        if self.str_attr_3 is not None:
            result['StrAttr3'] = self.str_attr_3

        if self.str_attr_4 is not None:
            result['StrAttr4'] = self.str_attr_4

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('Crop') is not None:
            self.crop = m.get('Crop')

        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')

        if m.get('IntAttr2') is not None:
            self.int_attr_2 = m.get('IntAttr2')

        if m.get('IntAttr3') is not None:
            self.int_attr_3 = m.get('IntAttr3')

        if m.get('IntAttr4') is not None:
            self.int_attr_4 = m.get('IntAttr4')

        if m.get('PicContent') is not None:
            self.pic_content = m.get('PicContent')

        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')

        if m.get('StrAttr2') is not None:
            self.str_attr_2 = m.get('StrAttr2')

        if m.get('StrAttr3') is not None:
            self.str_attr_3 = m.get('StrAttr3')

        if m.get('StrAttr4') is not None:
            self.str_attr_4 = m.get('StrAttr4')

        return self

