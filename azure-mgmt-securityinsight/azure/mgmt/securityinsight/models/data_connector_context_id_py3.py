# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DataConnectorContextId(Model):
    """Describes an Azure resource with kind.

    :param context_id: The context id of the origin data source (Like
     tenantID, SubscriptionID etc.).
    :type context_id: str
    """

    _attribute_map = {
        'context_id': {'key': 'contextId', 'type': 'str'},
    }

    def __init__(self, *, context_id: str=None, **kwargs) -> None:
        super(DataConnectorContextId, self).__init__(**kwargs)
        self.context_id = context_id
