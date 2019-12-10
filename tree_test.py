#encoding=utf-8
from pyecharts import Tree

data = [
    {
        "children": [
            {
                "children": [],
                "name": "B"
            },
            {
                "children": [
                    {
                        "children": [
                            {
                                "children": [],
                                "name": "I"
                            }
                        ],
                        "name": "E"
                    },
                    {
                        "children": [],
                        "name": "F"
                    }
                ],
                "name": "C"
            },
            {
                "children": [
                    {
                        "children": [
                            {
                                "children": [],
                                "name": "J"
                            },
                            {
                                "children": [],
                                "name": "K"
                            }
                        ],
                        "name": "G"
                    },
                    {
                        "children": [],
                        "name": "H"
                    }
                ],
                "name": "D"
            }
        ],
        "name": "A"
    }
]

tree = Tree("树图示例")
tree.add("", data)
tree.render()
