# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkedmall20230930 import models as main_models
from darabonba.model import DaraModel

class DistributionProduct(DaraModel):
    def __init__(
        self,
        category_chain: str = None,
        category_leaf_id: int = None,
        category_leaf_name: str = None,
        channel_code: str = None,
        distribute_status: str = None,
        pic_url: str = None,
        product_id: str = None,
        seller_id: str = None,
        short_title: str = None,
        skus: List[main_models.DistributionSku] = None,
        title: str = None,
        white_background_pic_url: str = None,
    ):
        self.category_chain = category_chain
        self.category_leaf_id = category_leaf_id
        self.category_leaf_name = category_leaf_name
        self.channel_code = channel_code
        self.distribute_status = distribute_status
        self.pic_url = pic_url
        self.product_id = product_id
        self.seller_id = seller_id
        self.short_title = short_title
        self.skus = skus
        self.title = title
        self.white_background_pic_url = white_background_pic_url

    def validate(self):
        if self.skus:
            for v1 in self.skus:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_chain is not None:
            result['categoryChain'] = self.category_chain

        if self.category_leaf_id is not None:
            result['categoryLeafId'] = self.category_leaf_id

        if self.category_leaf_name is not None:
            result['categoryLeafName'] = self.category_leaf_name

        if self.channel_code is not None:
            result['channelCode'] = self.channel_code

        if self.distribute_status is not None:
            result['distributeStatus'] = self.distribute_status

        if self.pic_url is not None:
            result['picUrl'] = self.pic_url

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.seller_id is not None:
            result['sellerId'] = self.seller_id

        if self.short_title is not None:
            result['shortTitle'] = self.short_title

        result['skus'] = []
        if self.skus is not None:
            for k1 in self.skus:
                result['skus'].append(k1.to_map() if k1 else None)

        if self.title is not None:
            result['title'] = self.title

        if self.white_background_pic_url is not None:
            result['whiteBackgroundPicUrl'] = self.white_background_pic_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('categoryChain') is not None:
            self.category_chain = m.get('categoryChain')

        if m.get('categoryLeafId') is not None:
            self.category_leaf_id = m.get('categoryLeafId')

        if m.get('categoryLeafName') is not None:
            self.category_leaf_name = m.get('categoryLeafName')

        if m.get('channelCode') is not None:
            self.channel_code = m.get('channelCode')

        if m.get('distributeStatus') is not None:
            self.distribute_status = m.get('distributeStatus')

        if m.get('picUrl') is not None:
            self.pic_url = m.get('picUrl')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('sellerId') is not None:
            self.seller_id = m.get('sellerId')

        if m.get('shortTitle') is not None:
            self.short_title = m.get('shortTitle')

        self.skus = []
        if m.get('skus') is not None:
            for k1 in m.get('skus'):
                temp_model = main_models.DistributionSku()
                self.skus.append(temp_model.from_map(k1))

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('whiteBackgroundPicUrl') is not None:
            self.white_background_pic_url = m.get('whiteBackgroundPicUrl')

        return self

