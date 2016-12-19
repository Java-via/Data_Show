/**
 * Created by user on 2016/11/24.
 */

function param_click(div_background, div_popup, div_title, params) {
    div_background.width($(document).width());
    div_background.height($(window).height());
    div_background.show();

    loadChart(params.name);
    div_popup.fadeIn(200);
    div_title.text(params.name);
    $('body').animate().css("overflow", "hidden");
    event.stopPropagation();

    div_background.click(function (){
        div_background.hide();
        div_popup.slideUp(300);
        $('body').animate().css("overflow", "auto");
    });

}

function make_pie() {
    var option = {
        tooltip: {
            trigger: 'item'
        },
        legend: {
            orient: 'vertical',
            x: 'left',
            data:['直接访问','邮件营销','联盟广告','视频广告','搜索引擎']
        },
        series: [
            {
                name:'访问来源',
                type:'pie',
                radius: ['50%', '70%'],
                avoidLabelOverlap: false,
                label: {
                    normal: {
                        show: false,
                        position: 'center'
                    },
                    emphasis: {
                        show: true,
                        textStyle: {
                            fontSize: '30',
                            fontWeight: 'bold'
                        }
                    }
                },
                labelLine: {
                    normal: {
                        show: false
                    }
                },
                data:[
                    {value:335, name:'直接访问'},
                    {value:310, name:'邮件营销'},
                    {value:234, name:'联盟广告'},
                    {value:135, name:'视频广告'},
                    {value:1548, name:'搜索引擎'}
                ]
            }
        ]
    };
    return option;
}

function make_line_country() {
    var option_line = {
        title: {
            text: '各分数段电影数量',
            left: 'center',
            top: 'top'
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data:['总数','美国','英国', '中国','韩国', '日本'],
            left:'center',
            top: 'bottom'
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '10%',
            containLabel: true
        },
        // toolbox: {
        //     feature: {
        //         dataView:{readOnly: true},
        //         saveAsImage: {show: true}
        //     }
        // },
        xAxis: {
            type: 'category',
            axisTick: {
                alignWithLabel: true
            },
            data: ['9+', '8+', '7+', '6+', '5+', '4+', '3+', '2+', '1+', '0+']
        },
        yAxis: {
            type: 'value',
            name: '数量',
            position: 'left',
            axisLabel: {
                formatter: '{value} 部'
            }
        },
        series: [
            {
                name:'总数',
                type:'line',
                data:[1088, 4589, 5947, 3741, 1305, 400, 199, 40, 0, 0]
            },
            {
                name:'各级别数量',
                type:'bar',
                itemStyle: {
                    normal: {
                        color: '#334b5c'
                    }
                },
                data:[1088, 4589, 5947, 3741, 1305, 400, 199, 40, 0, 0]
            },
            {
                name:'美国',
                type:'bar',
                barWidth : 8,
                itemStyle: {
                    normal: {
                        color: '#9dc6b3'
                    }
                },
                stack: '各级别数量',
                data:[414, 1439, 1997, 1346, 437, 72, 13, 0, 0, 0]
            },
            {
                name:'英国',
                type:'bar',
                itemStyle: {
                    normal: {
                        color: '#d1917b'
                    }
                },
                stack: '各级别数量',
                data:[196, 532, 531, 270, 65, 8, 4, 0, 0, 0]
            },
            {
                name:'中国',
                type:'bar',
                itemStyle: {
                    normal: {
                        color: '#77a9ae'
                    }
                },
                stack: '各级别数量',
                data:[124, 739, 1470, 1242, 581, 289, 179, 38, 0, 0]
            },
            {
                name:'韩国',
                type:'bar',
                itemStyle: {
                    normal: {
                        color: '#f8b758'
                    }
                },
                stack: '各级别数量',
                data:[30, 169, 371, 348, 103, 20, 6, 1, 0, 0]
            },
            {
                name:'日本',
                type:'bar',
                itemStyle: {
                    normal: {
                        color: '#37b158'
                    }
                },
                stack: '各级别数量',
                data:[286, 1230, 1118, 492, 125, 24, 5, 1, 0, 0]
            }
        ]
    };
    return option_line;
}

function make_map_country() {
    var option = {
        title: {
            text: '2016年各国电影数量盘点',
// {#                            subtext: 'from United Nations, Total population, both sexes combined, as of 1 July (thousands)',#}
// {#                            sublink: 'http://esa.un.org/wpp/Excel-Data/population.htm',#}
            left: 'center',
            top: 'top'
        },
        tooltip: {
            trigger: 'item',
            formatter: function (params) {
                var value = params.value;
                return params.seriesName + '<br/>' + params.name + ' : ' + value;
            }
        },
        // toolbox: {
        //     show: true,
        //     orient: 'vertical',
        //     left: 'right',
        //     top: 'center',
        //     feature: {
        //         dataView: {readOnly: false},
        //         restore: {},
        //         saveAsImage: {}
        //     }
        // },
        visualMap: {
            min: 0,
            max: 1400,
            splitNumber: 5,
            color: ['#d94e5d','#eac736','#50a3ba']
// {#                            min: 0,#}
// {#                            max: 1400,#}
// {#                            text:['高','低'],#}
// {#                            realtime: false,#}
// {#                            calculable: true,#}
// {#                            inRange: {#}
// {#                                color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']#}
// {#                            }#}
        },

        series: [
            {
                name: '各国电影产量 (2016)',
                type: 'map',
                mapType: 'world',
                roam: true,
                itemStyle:{
                    emphasis:{label:{show:true}}
                },
                nameMap: {
                    'China': "中国",
                    'United States of America': "美国",
                    'Japan': "日本",
                    'United Kingdom': "英国",

                    'France': "法国",
                    'South Korea': "韩国",
                    'North Korea': "韩国",
                    'Germany': "德国",
                    'Italy': "意大利",

                    'India': "印度",
                    'Thailand': "泰国",
                    'Spain': "西班牙",
                    'Canada': "加拿大",

                    'Australia': "澳大利亚",
                    'Russia': "俄罗斯",
                    'Iran': "伊朗",
                    'Ireland': "爱尔兰",

                    'Sweden': "瑞典",
                    'Brazil': "巴西",
                    'Denmark': "丹麦",
                    'Poland': "波兰",

                    'Czech Republic': "捷克",
                    'Argentina': "阿根廷",
                    'Belgium': "比利时",
                    'Mexico': "墨西哥",

                    'New Zealand': "新西兰",
                    'Netherlands': "荷兰",
                    'Austria': "奥地利",
                    'Turkey': "土耳其",

                    'Hungary': "匈牙利",
                    'Israel': "以色列"
                },
                data:[
                    {name: '中国', value: 1398},
                    {name: '美国', value: 916},
                    {name: '日本', value: 691.000},
                    {name: '英国', value: 296.000},

                    {name: '法国', value: 160.000},
                    {name: '韩国', value: 313.000},
                    {name: '德国', value: 80.000},
                    {name: '意大利', value: 28.000},

                    {name: '印度', value: 46.000},
                    {name: '泰国', value: 76.000},
                    {name: '西班牙', value: 32.000},
                    {name: '加拿大', value: 52.000},

                    {name: '澳大利亚', value: 23.000},
                    {name: '俄罗斯', value: 15.000},
                    {name: '伊朗', value: 9.000},
                    {name: '爱尔兰', value: 10.000},

                    {name: '瑞典', value: 14.000},
                    {name: '巴西', value: 13.000},
                    {name: '丹麦', value: 13.000},
                    {name: '波兰', value: 12.000},

                    {name: '捷克', value: 10.000},
                    {name: '阿根廷', value: 8.000},
                    {name: '比利时', value: 21.000},
                    {name: '墨西哥', value: 6.000},

                    {name: '新西兰', value: 5.000},
                    {name: '荷兰', value: 12.000},
                    {name: '奥地利', value: 12.000},
                    {name: '土耳其', value: 3.000},

                    {name: '匈牙利', value: 5.000},
                    {name: '以色列', value: 6.000}
                ]
            }
        ]
    };
    return option;
}

function make_pie(text, dict_country) {
    console.log(dict_country);
    var option = {
        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b}: {c} ({d}%)"
        },
        legend: {
            orient: 'vertical',
            x: 'left',
            silent: true,
            data:['8.5+','7+','5.5+','5.5-','其他']
        },
        series: [
            {
                name:'访问来源',
                type:'pie',
                silent: false,
                radius: ['50%', '70%'],
                avoidLabelOverlap: false,
                label: {
                    normal: {
                        show: false,
                        position: 'center'
                    },
                    emphasis: {
                        show: true,
                        textStyle: {
                            fontSize: '30',
                            fontWeight: 'bold'
                        }
                    }
                },
                labelLine: {
                    normal: {
                        show: true
                    }
                },
                data:[
                    {
                        value:dict_country[text][0],
                        name:'8.5+'
                    },
                    {
                        value:dict_country[text][1],
                        name:'7+'
                    },
                    {
                        value:dict_country[text][2],
                        name:'5.5+'
                    },
                    {
                        value:dict_country[text][3],
                        name:'5.5-'
                    },
                    {
                        value:dict_country[text][4],
                        name:'其他',
                        itemStyle: {
                            normal: {
                                color: '#37b158'
                            }
                        }
                    }
                ]
            }
        ]
    };
    return option;
}

function make_highrate_line() {
    var option = {
        title: {
            text: '世界高分电影占比变化',
            left: 'center',
            top: 'top'
        },
        tooltip: {
            trigger: 'axis'
        },
        // legend: {
        //     data:['高分电影占比']
        // },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        // toolbox: {
        //     feature: {
        //         dataView:{readOnly: true},
        //         saveAsImage: {}
        //     }
        // },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: ['1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']
        },
        yAxis: {
            type: 'value',
            axisLabel: {
                formatter: '{value} %'
            }
        },
        series: [
            {
                name:'高分电影占比',
                type:'line',
                stack: '总量',
                data:[9.24, 10.24, 8.51, 4.05, 4.71, 5.29, 8.43, 6.73, 6.1, 8.3, 7.34, 6.54, 4.64, 5.11, 6.76, 6.21, 5.27, 7.53, 7.71, 5.54, 6.07, 5.99, 7.49, 7.29, 6.59, 4.76, 5.79, 5.04, 6.71]
            }
        ]
    };
    return option;
}

function make_count_world() {
    var option = {
        title: {
            text: '世界电影数量变化',
            top: 'top',
            left: 'center'
        },

        tooltip: {
            trigger: 'axis'
        },
        // legend: {
        //     data:['电影数量']
        // },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        // toolbox: {
        //     feature: {
        //         dataView:{readOnly: true},
        //         saveAsImage: {}
        //     }
        // },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: ['1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']
        },
        yAxis: {
            type: 'value',
            axisLabel: {
                formatter: '{value} 部'
            }
        },
        series: [
            {
                name:'电影数量',
                type:'line',
                data:[119, 127, 141, 148, 170, 208, 178, 208, 213, 265, 259, 306, 323, 352, 429, 451, 531, 611, 713, 813, 889, 951, 975, 1042, 1092, 1135, 1174, 1112, 671]
            }
        ]
    };
    return option;
}

function make_high_count_china() {
    var option = {
        title: {
            text: '中国电影数量变化',
            left: 'center',
            top: 'top'
        },

        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data:['电影数量', '高分占比'],
            top: 'bottom'
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '10%',
            containLabel: true
        },
        // toolbox: {
        //     feature: {
        //         dataView:{readOnly: true},
        //         saveAsImage: {}
        //     }
        // },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']
        },
        yAxis: [
            {
                type: 'value',
                name: '高分占比',
                max: 10,
                axisLabel: {
                    formatter: '{value} %'
                }
            },
            {
                type: 'value',
                name: '电影数量',
                axisLabel: {
                    formatter: '{value} 部'
                }
            }

        ],
        series: [
            {
                name:'电影数量',
                itemStyle: {
                    normal: {
                        color: '#50a3ba'
                    }
                },
                yAxisIndex: 1,
                type:'line',
                data:[116, 113, 136, 128, 143, 129, 146, 162, 166, 199, 224, 222, 263, 271, 311, 341, 264]
            },
            {
                name:'高分占比',
                type:'line',
                itemStyle: {
                    normal: {
                        color: '#d94e5d'
                    }
                },
                data:[3.45, 1.77, 1.47, 1.56, 2.1, 3.88, 3.42, 0.62, 2.41, 3.52, 4.91, 1.8, 2.28, 2.21, 2.25, 3.81, 1.89]
            }
        ]
    };
    return option;
}

function make_high_count_america() {
    var option = {
        title: {
            text: '美国电影数量变化',
            top: 'top',
            left: 'center'
        },

        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data:['电影数量', '高分占比'],
            left: 'center',
            top: 'bottom'
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '10%',
            containLabel: true
        },
        // toolbox: {
        //     feature: {
        //         dataView:{readOnly: true},
        //         saveAsImage: {}
        //     }
        // },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: ['1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']
        },
        yAxis: [
            {
                type: 'value',
                name: '高分占比',
                axisLabel: {
                    formatter: '{value} %'
                }
            },
            {
                type: 'value',
                name: '电影数量',
                axisLabel: {
                    formatter: '{value} 部'
                }
            }

        ],
        series: [
            {
                name:'电影数量',
                itemStyle: {
                    normal: {
                        color: '#50a3ba'
                    }
                },
                yAxisIndex: 1,
                type:'line',
                data:[34, 41, 43, 41, 49, 69, 54, 77, 74, 98, 96, 107, 119, 129, 149, 159, 173, 231, 243, 292, 310, 327, 316, 358, 328, 343, 368, 321, 184]
            },
            {
                name:'高分占比',
                type:'line',
                itemStyle: {
                    normal: {
                        color: '#d94e5d'
                    }
                },
                data:[11.76, 9.76, 9.3, 7.32, 10.2, 7.25, 9.26, 5.19, 5.41, 10.2, 5.21, 9.35, 6.72, 6.2, 8.72, 8.81, 6.94, 8.66, 6.58, 6.85, 6.13, 5.5, 8.54, 9.22, 7.93, 4.96, 7.07, 6.23, 11.96]
            }
        ]
    };
    return option;
}

function make_china_america() {
    var option = {
        title: {
            text: '美国与中国电影比较'
        },

        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data:['美国高分占比', '中国高分占比']
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        // toolbox: {
        //     feature: {
        //         dataView:{readOnly: true},
        //         saveAsImage: {}
        //     }
        // },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: ['1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']
        },
        yAxis: [
            {
                type: 'value',
                name: '美国高分占比',
                axisLabel: {
                    formatter: '{value} %'
                }
            }
        ],
        series: [
            {
                name:'美国高分占比',
                itemStyle: {
                    normal: {
                        color: '#50a3ba'
                    }
                },
                type:'line',
                data: [11.76, 9.76, 9.3, 7.32, 10.2, 7.25, 9.26, 5.19, 5.41, 10.2, 5.21, 9.35, 6.72, 6.2, 8.72, 8.81, 6.94, 8.66, 6.58, 6.85, 6.13, 5.5, 8.54, 9.22, 7.93, 4.96, 7.07, 6.23, 11.96]
            },
            {
                name:'中国高分占比',
                type:'line',
                itemStyle: {
                    normal: {
                        color: '#d94e5d'
                    }
                },
                data:[3.85, 3.7, 1.59, 0.0, 3.85, 2.17, 7.5, 4.0, 0.0, 3.49, 1.32, 3.23, 3.45, 1.77, 1.47, 1.56, 2.1, 3.88, 3.42, 0.62, 2.41, 3.52, 4.91, 1.8, 2.28, 2.21, 2.25, 3.81, 1.89]
            }
        ]
    };
    return option;
}

