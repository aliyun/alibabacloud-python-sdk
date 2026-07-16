# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateImageRequest(DaraModel):
    def __init__(
        self,
        custom_content: str = None,
        instance_name: str = None,
        int_attr: int = None,
        int_attr_2: int = None,
        int_attr_3: int = None,
        int_attr_4: int = None,
        pic_name: str = None,
        product_id: str = None,
        str_attr: str = None,
        str_attr_2: str = None,
        str_attr_3: str = None,
        str_attr_4: str = None,
    ):
        # The custom content. The content can be up to 4,096 characters in length.
        # >This field is returned when you call the "<props="china">[SearchImageByPic](https://help.aliyun.com/document_detail/202282.html)<props="intl">[SearchImageByPic](https://www.alibabacloud.com/help/zh/image-search/latest/updateimage)" operation. For example, you can add text such as image descriptions.
        self.custom_content = custom_content
        # The name of the Image Search instance. The name can be up to 20 characters in length.
        # If you have purchased an Image Search instance, go to the [Image Search console](https://imagesearch.console.aliyun.com/) to view the instance name.
        # If you have not purchased an Image Search instance, see [Activate the service](https://help.aliyun.com/document_detail/179178.html) and [Create an instance](https://help.aliyun.com/document_detail/66569.html).
        # >The instance name is not the instance ID. Make sure to distinguish between them.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The integer attribute. This attribute can be used to filter query results. This field is returned in query results.
        self.int_attr = int_attr
        # The integer attribute. This attribute can be used to filter query results. This field is returned in query results.
        self.int_attr_2 = int_attr_2
        # The integer attribute. This attribute can be used to filter query results. This field is returned in query results.
        self.int_attr_3 = int_attr_3
        # The integer attribute. This attribute can be used to filter query results. This field is returned in query results.
        self.int_attr_4 = int_attr_4
        # The image name. The name can be up to 256 characters in length.
        # > - The combination of ProductId and PicName uniquely identifies an image.
        # - If you add an image multiple times with the same ProductId and PicName, the most recently added image takes effect and the previously added images are replaced.
        self.pic_name = pic_name
        # The product ID. The ID can be up to 256 characters in length.
        # 
        # >A product can have multiple images. You can customize the value of this parameter based on your business requirements. For example: top001, pants002.
        # 
        # This parameter is required.
        self.product_id = product_id
        # The string attribute. The attribute can be up to 128 characters in length. It can be used to filter query results. This field is returned in query results.
        self.str_attr = str_attr
        # The string attribute. The attribute can be up to 128 characters in length. It can be used to filter query results. This field is returned in query results.
        self.str_attr_2 = str_attr_2
        # The string attribute. The attribute can be up to 128 characters in length. It can be used to filter query results. This field is returned in query results.
        self.str_attr_3 = str_attr_3
        # The string attribute. The attribute can be up to 128 characters in length. It can be used to filter query results. This field is returned in query results.
        self.str_attr_4 = str_attr_4

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.pic_name is not None:
            result['PicName'] = self.pic_name

        if self.product_id is not None:
            result['ProductId'] = self.product_id

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

        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')

        if m.get('StrAttr2') is not None:
            self.str_attr_2 = m.get('StrAttr2')

        if m.get('StrAttr3') is not None:
            self.str_attr_3 = m.get('StrAttr3')

        if m.get('StrAttr4') is not None:
            self.str_attr_4 = m.get('StrAttr4')

        return self

