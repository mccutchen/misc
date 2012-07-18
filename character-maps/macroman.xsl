<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

	<!-- Output parameters -->
	<xsl:output
        method="text"
        encoding="utf-8"
        byte-order-mark="no" />
    
    <!-- template:
         <xsl:output-character character="&#x0080;" string="&lt;\#128&gt;" /> <? <control> ?>
     -->
    
    <xsl:template match="/">
        
        <xsl:text>&lt;xsl:character-map name="unicode-to-macroman"&gt;</xsl:text>
        <xsl:call-template name="break" />
        
        <xsl:apply-templates select="//tr" />
        
        <xsl:text>&lt;/xsl:character-map&gt;</xsl:text>
    </xsl:template>
    
    <xsl:template match="tr">
        
        <xsl:variable name="unicode" select="concat('&amp;#x', normalize-space(substring(td[5], 3)), ';')" />
        <xsl:variable name="macroman" select="concat('&amp;lt;\#', td[2], '&amp;gt;')" />
        <xsl:variable name="character-name" select="td[7]" />
        
        <xsl:call-template name="sep" />
        
        <xsl:text>&lt;xsl:output-character character="</xsl:text>
        <xsl:value-of select="$unicode" />
        <xsl:text>" string="</xsl:text>
        <xsl:value-of select="$macroman" />
        <xsl:text>" /&gt; &lt;!-- </xsl:text>
        <xsl:value-of select="$character-name" />
        <xsl:text> --&gt;</xsl:text>
        
        <xsl:call-template name="break" />
    </xsl:template>
	
	
    <xsl:template name="sep">
        <xsl:text>&#9;</xsl:text>
    </xsl:template>
    
    <xsl:template name="break">
        <xsl:text>&#13;&#10;</xsl:text>
    </xsl:template>

</xsl:stylesheet>