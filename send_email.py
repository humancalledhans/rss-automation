from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient
import os

# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python


def send_email():
    message = Mail(
        # from_email='info@instalitica.com',
        from_email='dp@pounciltech.com',
        to_emails='workhansyap@gmail.com',
        subject='test email',
        # template_id="d-1b2f3672ad08468991fee793a884a4e3",
        html_content='''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html data-editor-version="2" class="sg-campaigns" xmlns="http://www.w3.org/1999/xhtml">
    <head>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1">
      <!--[if !mso]><!-->
      <meta http-equiv="X-UA-Compatible" content="IE=Edge">
      <!--<![endif]-->
      <!--[if (gte mso 9)|(IE)]>
      <xml>
        <o:OfficeDocumentSettings>
          <o:AllowPNG/>
          <o:PixelsPerInch>96</o:PixelsPerInch>
        </o:OfficeDocumentSettings>
      </xml>
      <![endif]-->
      <!--[if (gte mso 9)|(IE)]>
  <style type="text/css">
    body {width: 800px;margin: 0 auto;}
    table {border-collapse: collapse;}
    table, td {mso-table-lspace: 0pt;mso-table-rspace: 0pt;}
    img {-ms-interpolation-mode: bicubic;}
  </style>
<![endif]-->
      <style type="text/css">
    body, p, div {
      font-family: arial,helvetica,sans-serif;
      font-size: 14px;
    }
    body {
      color: #000000;
    }
    body a {
      color: #487995;
      text-decoration: none;
    }
    p { margin: 0; padding: 0; }
    table.wrapper {
      width:100% !important;
      table-layout: fixed;
      -webkit-font-smoothing: antialiased;
      -webkit-text-size-adjust: 100%;
      -moz-text-size-adjust: 100%;
      -ms-text-size-adjust: 100%;
    }
    img.max-width {
      max-width: 100% !important;
    }
    .column.of-2 {
      width: 50%;
    }
    .column.of-3 {
      width: 33.333%;
    }
    .column.of-4 {
      width: 25%;
    }
    ul ul ul ul  {
      list-style-type: disc !important;
    }
    ol ol {
      list-style-type: lower-roman !important;
    }
    ol ol ol {
      list-style-type: lower-latin !important;
    }
    ol ol ol ol {
      list-style-type: decimal !important;
    }
    @media screen and (max-width:480px) {
      .preheader .rightColumnContent,
      .footer .rightColumnContent {
        text-align: left !important;
      }
      .preheader .rightColumnContent div,
      .preheader .rightColumnContent span,
      .footer .rightColumnContent div,
      .footer .rightColumnContent span {
        text-align: left !important;
      }
      .preheader .rightColumnContent,
      .preheader .leftColumnContent {
        font-size: 80% !important;
        padding: 5px 0;
      }
      table.wrapper-mobile {
        width: 100% !important;
        table-layout: fixed;
      }
      img.max-width {
        height: auto !important;
        max-width: 100% !important;
      }
      a.bulletproof-button {
        display: block !important;
        width: auto !important;
        font-size: 80%;
        padding-left: 0 !important;
        padding-right: 0 !important;
      }
      .columns {
        width: 100% !important;
      }
      .column {
        display: block !important;
        width: 100% !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
        margin-left: 0 !important;
        margin-right: 0 !important;
      }
      .social-icon-column {
        display: inline-block !important;
      }
    }
  </style>
      <!--user entered Head Start--><!--End Head user entered-->
    </head>
    <body>
      <center class="wrapper" data-link-color="#487995" data-body-style="font-size:14px; font-family:arial,helvetica,sans-serif; color:#000000; background-color:#edf1f3;">
        <div class="webkit">
          <table cellpadding="0" cellspacing="0" border="0" width="100%" class="wrapper" bgcolor="#edf1f3">
            <tr>
              <td valign="top" bgcolor="#edf1f3" width="100%">
                <table width="100%" role="content-container" class="outer" align="center" cellpadding="0" cellspacing="0" border="0">
                  <tr>
                    <td width="100%">
                      <table width="100%" cellpadding="0" cellspacing="0" border="0">
                        <tr>
                          <td>
                            <!--[if mso]>
    <center>
    <table><tr><td width="800">
  <![endif]-->
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="width:100%; max-width:800px;" align="center">
                                      <tr>
                                        <td role="modules-container" style="padding:0px 0px 0px 0px; color:#000000; text-align:left;" bgcolor="#EDF1F3" width="100%" align="left"><table class="module preheader preheader-hide" role="module" data-type="preheader" border="0" cellpadding="0" cellspacing="0" width="100%" style="display: none !important; mso-hide: all; visibility: hidden; opacity: 0; color: transparent; height: 0; width: 0;">
    <tr>
      <td role="module-content">
        <p></p>
      </td>
    </tr>
  </table><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="7d396aee-5888-4f7d-a788-6ff13a7ac450" data-mc-module-version="2019-10-22">
    <tbody>
      <tr>
        <td style="padding:15px 0px 15px 100px; line-height:14px; text-align:inherit;" height="100%" valign="top" bgcolor="" role="module-content"><div><div style="font-family: inherit; text-align: right"><span style="font-family: verdana, geneva, sans-serif; color: #84b0ca; font-size: 10px">Email not displaying correctly? </span><span style="font-family: verdana, geneva, sans-serif; color: #0a3752; font-size: 10px"><strong>VIEW IT</strong></span><span style="font-family: verdana, geneva, sans-serif; color: #84b0ca; font-size: 10px"> in your browser.</span></div><div></div></div></td>
      </tr>
    </tbody>
  </table><table class="wrapper" role="module" data-type="image" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="b7993751-904f-45c7-a777-4b216693fc6d">
    <tbody>
      <tr>
        <td style="font-size:6px; line-height:10px; padding:0px 0px 0px 0px;" valign="top" align="center">
          <img class="max-width" border="0" style="display:block; color:#000000; text-decoration:none; font-family:Helvetica, arial, sans-serif; font-size:16px; max-width:100% !important; width:100%; height:auto !important;" width="800" alt="" data-proportionally-constrained="true" data-responsive="true" src="http://cdn.mcauto-images-production.sendgrid.net/c31721ac5f4f8b45/cf5fe532-da1d-42d2-9850-5918838dca3e/2447x1335.jpg">
        </td>
      </tr>
    </tbody>
  </table><table border="0" cellpadding="0" cellspacing="0" align="center" width="100%" role="module" data-type="columns" style="padding:0px 0px 0px 0px;" bgcolor="#0A3752" data-distribution="1,3">
    <tbody>
      <tr role="module-content">
        <td height="100%" valign="top"><table width="200" style="width:200px; border-spacing:0; border-collapse:collapse; margin:0px 0px 0px 0px;" cellpadding="0" cellspacing="0" align="left" border="0" bgcolor="" class="column column-0">
      <tbody>
        <tr>
          <td style="padding:0px;margin:0px;border-spacing:0;"><table class="wrapper" role="module" data-type="image" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="65da1b10-ac95-4c58-8705-320f7fbc84ff">
    <tbody>
      <tr>
        <td style="font-size:6px; line-height:10px; padding:35px 0px 35px 0px;" valign="top" align="center">
          <img class="max-width" border="0" style="display:block; color:#000000; text-decoration:none; font-family:Helvetica, arial, sans-serif; font-size:16px; max-width:70% !important; width:70%; height:auto !important;" width="140" alt="" data-proportionally-constrained="true" data-responsive="true" src="http://cdn.mcauto-images-production.sendgrid.net/c31721ac5f4f8b45/3f3180b7-e052-41ee-816e-c0201a80fda5/988x189.png">
        </td>
      </tr>
    </tbody>
  </table></td>
        </tr>
      </tbody>
    </table><table width="600" style="width:600px; border-spacing:0; border-collapse:collapse; margin:0px 0px 0px 0px;" cellpadding="0" cellspacing="0" align="left" border="0" bgcolor="" class="column column-1">
      <tbody>
        <tr>
          <td style="padding:0px;margin:0px;border-spacing:0;"><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="13845f09-d902-4cd1-9399-98b9b232b28e" data-mc-module-version="2019-10-22">
    <tbody>
      <tr>
        <td style="padding:30px 0px 0px 50px; line-height:30px; text-align:inherit; background-color:#84B0CA;" height="100%" valign="top" bgcolor="#84B0CA" role="module-content"><div><div style="font-family: inherit; text-align: left"><span style="color: #ffffff; font-family: verdana, geneva, sans-serif; font-size: 20px">Welcome to</span></div>
<div style="font-family: inherit; text-align: left"><span style="color: #ffffff; font-family: verdana, geneva, sans-serif; font-size: 30px"><strong>Chavez Real Estate Group</strong></span></div><div></div></div></td>
      </tr>
    </tbody>
  </table><table class="module" role="module" data-type="divider" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="b6dd84b3-f628-481f-9cde-68540200866a">
    <tbody>
      <tr>
        <td style="padding:10px 400px 10px 50px;" role="module-content" height="100%" valign="top" bgcolor="#84B0CA">
          <table border="0" cellpadding="0" cellspacing="0" align="center" width="100%" height="1px" style="line-height:1px; font-size:1px;">
            <tbody>
              <tr>
                <td style="padding:0px 0px 1px 0px;" bgcolor="#0A3752"></td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
    </tbody>
  </table><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="13845f09-d902-4cd1-9399-98b9b232b28e.1" data-mc-module-version="2019-10-22">
    <tbody>
      <tr>
        <td style="padding:10px 50px 20px 50px; line-height:24px; text-align:inherit; background-color:#84B0CA;" height="100%" valign="top" bgcolor="#84B0CA" role="module-content"><div><div style="font-family: inherit; text-align: left"><span style="font-family: verdana, geneva, sans-serif; font-size: 16px; color: #0a3752">Ready to find your dream home? Work with our team of real estate experts to locate the home you've always wanted. We'll work with your taste, budget, and schedule to make the process painless and easy (and, dare we say: fun).</span></div><div></div></div></td>
      </tr>
    </tbody>
  </table><table border="0" cellpadding="0" cellspacing="0" class="module" data-role="module-button" data-type="button" role="module" style="table-layout:fixed;" width="100%" data-muid="fbdc9861-d9a1-45ad-96f3-63a274aa47dd">
      <tbody>
        <tr>
          <td align="left" bgcolor="#84B0CA" class="outer-td" style="padding:0px 0px 0px 50px; background-color:#84B0CA;">
            <table border="0" cellpadding="0" cellspacing="0" class="wrapper-mobile" style="text-align:center;">
              <tbody>
                <tr>
                <td align="center" bgcolor="#0A3752" class="inner-td" style="border-radius:6px; font-size:16px; text-align:left; background-color:inherit;">
                  <a href="" style="background-color:#0A3752; border:0px solid #ffffff; border-color:#ffffff; border-radius:0px; border-width:0px; color:#ffffff; display:inline-block; font-size:14px; font-weight:normal; letter-spacing:0px; line-height:normal; padding:12px 30px 12px 30px; text-align:center; text-decoration:none; border-style:solid; font-family:verdana,geneva,sans-serif;" target="_blank">Learn more</a>
                </td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
      </tbody>
    </table><table class="module" role="module" data-type="spacer" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="37af17d2-b76e-4fdc-9a53-79fe9b269633">
    <tbody>
      <tr>
        <td style="padding:0px 0px 50px 0px;" role="module-content" bgcolor="#84B0CA">
        </td>
      </tr>
    </tbody>
  </table></td>
        </tr>
      </tbody>
    </table></td>
      </tr>
    </tbody>
  </table><table class="module" role="module" data-type="spacer" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="ed7c2e1f-ef68-49cc-afb1-23a045b430e9">
    <tbody>
      <tr>
        <td style="padding:0px 0px 50px 0px;" role="module-content" bgcolor="">
        </td>
      </tr>
    </tbody>
  </table><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="1d851adc-6a65-456d-9ccb-e210013807d7" data-mc-module-version="2019-10-22">
    <tbody>
      <tr>
        <td style="padding:0px 0px 0px 50px; line-height:20px; text-align:inherit; background-color:#edf1f3;" height="100%" valign="top" bgcolor="#edf1f3" role="module-content"><div><div style="font-family: inherit; text-align: left"><span style="font-family: verdana, geneva, sans-serif; font-size: 16px; color: #84b0ca"><strong>TRENDING THIS WEEK</strong></span></div><div></div></div></td>
      </tr>
    </tbody>
  </table><table class="module" role="module" data-type="divider" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="01b58dd9-a5f9-447c-b64d-fca44d976dce">
    <tbody>
      <tr>
        <td style="padding:5px 50px 20px 50px;" role="module-content" height="100%" valign="top" bgcolor="">
          <table border="0" cellpadding="0" cellspacing="0" align="center" width="100%" height="5px" style="line-height:5px; font-size:5px;">
            <tbody>
              <tr>
                <td style="padding:0px 0px 5px 0px;" bgcolor="#84B0CA"></td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
    </tbody>
  </table><table border="0" cellpadding="0" cellspacing="0" align="center" width="100%" role="module" data-type="columns" style="padding:0px 50px 20px 50px;" bgcolor="#EDF1F3" data-distribution="1,2">
    <tbody>
      <tr role="module-content">
        <td height="100%" valign="top"><table width="220" style="width:220px; border-spacing:0; border-collapse:collapse; margin:0px 20px 0px 0px;" cellpadding="0" cellspacing="0" align="left" border="0" bgcolor="" class="column column-0">
      <tbody>
        <tr>
          <td style="padding:0px;margin:0px;border-spacing:0;"><table class="wrapper" role="module" data-type="image" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="cBiyKgSAf3sHzEQtGwL8gU">
    <tbody>
      <tr>
        <td style="font-size:6px; line-height:10px; padding:0px 0px 0px 0px;" valign="top" align="center">
          <img class="max-width" border="0" style="display:block; color:#000000; text-decoration:none; font-family:Helvetica, arial, sans-serif; font-size:16px; max-width:100% !important; width:100%; height:auto !important;" width="220" alt="" data-proportionally-constrained="true" data-responsive="true" src="http://cdn.mcauto-images-production.sendgrid.net/c31721ac5f4f8b45/c32e6a9f-07c9-435a-bfd3-87ef46feba51/2400x1600.jpg">
        </td>
      </tr>
    </tbody>
  </table></td>
        </tr>
      </tbody>
    </table><table width="440" style="width:440px; border-spacing:0; border-collapse:collapse; margin:0px 0px 0px 20px;" cellpadding="0" cellspacing="0" align="left" border="0" bgcolor="" class="column column-1">
      <tbody>
        <tr>
          <td style="padding:0px;margin:0px;border-spacing:0;"><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="nab3S7wZerNme5cK7ZVFZW" data-mc-module-version="2019-10-22">
    <tbody>
      <tr>
        <td style="padding:15px 0px 5px 0px; line-height:20px; text-align:inherit; background-color:#edf1f3;" height="100%" valign="top" bgcolor="#edf1f3" role="module-content"><div><div style="font-family: inherit; text-align: inherit"><span style="font-family: verdana, geneva, sans-serif; color: #0a3752; font-size: 20px"><strong>Contemporary Kitchens</strong></span></div><div></div></div></td>
      </tr>
    </tbody>
  </table><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="nab3S7wZerNme5cK7ZVFZW.1" data-mc-module-version="2019-10-22">
    <tbody>
      <tr>
        <td style="padding:0px 0px 18px 0px; line-height:20px; text-align:inherit; background-color:#edf1f3;" height="100%" valign="top" bgcolor="#edf1f3" role="module-content"><div><div style="font-family: inherit; text-align: inherit"><span style="font-family: verdana, geneva, sans-serif; color: #0a3752">The clean design fits into a contemporary lifestyle that many urbanites desire, giving the busy life a break for gathering with families and friends.</span></div><div></div></div></td>
      </tr>
    </tbody>
  </table></td>
        </tr>
      </tbody>
    </table></td>
      </tr>
    </tbody>
  </table><table class="module" role="module" data-type="divider" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="01b58dd9-a5f9-447c-b64d-fca44d976dce.2">
    <tbody>
      <tr>
        <td style="padding:0px 50px 0px 50px;" role="module-content" height="100%" valign="top" bgcolor="">
          <table border="0" cellpadding="0" cellspacing="0" align="center" width="100%" height="5px" style="line-height:5px; font-size:5px;">
            <tbody>
              <tr>
                <td style="padding:0px 0px 5px 0px;" bgcolor="#84B0CA"></td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
    </tbody>
  </table><table border="0" cellpadding="0" cellspacing="0" align="center" width="100%" role="module" data-type="columns" style="padding:20px 50px 20px 50px;" bgcolor="" data-distribution="2,1">
    <tbody>
      <tr role="module-content">
        <td height="100%" valign="top"><table width="440" style="width:440px; border-spacing:0; border-collapse:collapse; margin:0px 20px 0px 0px;" cellpadding="0" cellspacing="0" align="left" border="0" bgcolor="" class="column column-0">
      <tbody>
        <tr>
          <td style="padding:0px;margin:0px;border-spacing:0;"><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="t7affZnVRDfBkmAqcpYU4C" data-mc-module-version="2019-10-22">
    <tbody>
      <tr>
        <td style="padding:15px 0px 5px 0px; line-height:20px; text-align:inherit;" height="100%" valign="top" bgcolor="" role="module-content"><div><div style="font-family: inherit; text-align: inherit"><span style="color: #0a3752; font-family: verdana, geneva, sans-serif; font-size: 20px"><strong>Modern Rooms</strong></span></div><div></div></div></td>
      </tr>
    </tbody>
  </table><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="t7affZnVRDfBkmAqcpYU4C.1" data-mc-module-version="2019-10-22">
    <tbody>
      <tr>
        <td style="padding:0px 0px 18px 0px; line-height:20px; text-align:inherit;" height="100%" valign="top" bgcolor="" role="module-content"><div><div style="font-family: inherit; text-align: inherit"><span style="color: #0a3752; font-family: verdana, geneva, sans-serif">Our modern rooms feature the latest trends in home design, giving people an upscale atmosphere.</span></div><div></div></div></td>
      </tr>
    </tbody>
  </table></td>
        </tr>
      </tbody>
    </table><table width="220" style="width:220px; border-spacing:0; border-collapse:collapse; margin:0px 0px 0px 20px;" cellpadding="0" cellspacing="0" align="left" border="0" bgcolor="" class="column column-1">
      <tbody>
        <tr>
          <td style="padding:0px;margin:0px;border-spacing:0;"><table class="wrapper" role="module" data-type="image" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="8MK9EUGigZmF1RkDXwck3N">
    <tbody>
      <tr>
        <td style="font-size:6px; line-height:10px; padding:0px 0px 0px 0px;" valign="top" align="center">
          <img class="max-width" border="0" style="display:block; color:#000000; text-decoration:none; font-family:Helvetica, arial, sans-serif; font-size:16px; max-width:100% !important; width:100%; height:auto !important;" width="440" alt="" data-proportionally-constrained="true" data-responsive="true" src="http://cdn.mcauto-images-production.sendgrid.net/c31721ac5f4f8b45/b51100dd-1e37-4e44-9098-fbc015b62f03/2688x1792.jpg">
        </td>
      </tr>
    </tbody>
  </table></td>
        </tr>
      </tbody>
    </table></td>
      </tr>
    </tbody>
  </table><table class="module" role="module" data-type="divider" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="01b58dd9-a5f9-447c-b64d-fca44d976dce.1.1">
    <tbody>
      <tr>
        <td style="padding:0px 50px 0px 50px;" role="module-content" height="100%" valign="top" bgcolor="">
          <table border="0" cellpadding="0" cellspacing="0" align="center" width="100%" height="5px" style="line-height:5px; font-size:5px;">
            <tbody>
              <tr>
                <td style="padding:0px 0px 5px 0px;" bgcolor="#84B0CA"></td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
    </tbody>
  </table><table border="0" cellpadding="0" cellspacing="0" align="center" width="100%" role="module" data-type="columns" style="padding:20px 50px 20px 50px;" bgcolor="" data-distribution="1,2">
    <tbody>
      <tr role="module-content">
        <td height="100%" valign="top"><table width="220" style="width:220px; border-spacing:0; border-collapse:collapse; margin:0px 20px 0px 0px;" cellpadding="0" cellspacing="0" align="left" border="0" bgcolor="" class="column column-0">
      <tbody>
        <tr>
          <td style="padding:0px;margin:0px;border-spacing:0;"><table class="wrapper" role="module" data-type="image" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="8s5S4vEMmEFFvEACaAdQnT">
    <tbody>
      <tr>
        <td style="font-size:6px; line-height:10px; padding:0px 0px 0px 0px;" valign="top" align="center">
          <img class="max-width" border="0" style="display:block; color:#000000; text-decoration:none; font-family:Helvetica, arial, sans-serif; font-size:16px; max-width:100% !important; width:100%; height:auto !important;" width="220" alt="" data-proportionally-constrained="true" data-responsive="true" src="http://cdn.mcauto-images-production.sendgrid.net/c31721ac5f4f8b45/5608b7f6-d221-460a-8f36-ed10fd78a08a/2700x1800.jpg">
        </td>
      </tr>
    </tbody>
  </table></td>
        </tr>
      </tbody>
    </table><table width="440" style="width:440px; border-spacing:0; border-collapse:collapse; margin:0px 0px 0px 20px;" cellpadding="0" cellspacing="0" align="left" border="0" bgcolor="" class="column column-1">
      <tbody>
        <tr>
          <td style="padding:0px;margin:0px;border-spacing:0;"><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="d58MX5emqUnAkiXJRGcuVd" data-mc-module-version="2019-10-22">
    <tbody>
      <tr>
        <td style="padding:15px 0px 18px 0px; line-height:20px; text-align:inherit;" height="100%" valign="top" bgcolor="" role="module-content"><div><div style="font-family: inherit; text-align: inherit"><span style="color: #0a3752; font-family: verdana, geneva, sans-serif; font-size: 20px"><strong>Traditional Dining Rooms</strong></span></div><div></div></div></td>
      </tr>
    </tbody>
  </table><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="d58MX5emqUnAkiXJRGcuVd.1" data-mc-module-version="2019-10-22">
    <tbody>
      <tr>
        <td style="padding:0px 0px 18px 0px; line-height:20px; text-align:inherit;" height="100%" valign="top" bgcolor="" role="module-content"><div><div style="font-family: inherit; text-align: inherit"><span style="color: #0a3752; font-family: verdana, geneva, sans-serif">The tradition never goes away. We are experts in treasuring and decorating the house with whatever tradition speaks to you.</span></div><div></div></div></td>
      </tr>
    </tbody>
  </table></td>
        </tr>
      </tbody>
    </table></td>
      </tr>
    </tbody>
  </table><table class="module" role="module" data-type="spacer" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="c2f7a2d5-91ec-45f0-8519-5264163797c0">
    <tbody>
      <tr>
        <td style="padding:0px 0px 20px 0px;" role="module-content" bgcolor="">
        </td>
      </tr>
    </tbody>
  </table><table border="0" cellpadding="0" cellspacing="0" align="center" width="100%" role="module" data-type="columns" style="padding:0px 0px 0px 0px;" bgcolor="#84B0CA" data-distribution="1,1,1">
    <tbody>
      <tr role="module-content">
        <td height="100%" valign="top"><table width="266" style="width:266px; border-spacing:0; border-collapse:collapse; margin:0px 0px 0px 0px;" cellpadding="0" cellspacing="0" align="left" border="0" bgcolor="" class="column column-0">
      <tbody>
        <tr>
          <td style="padding:0px;margin:0px;border-spacing:0;"><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="1d851adc-6a65-456d-9ccb-e210013807d7.1" data-mc-module-version="2019-10-22">
    <tbody>
      <tr>
        <td style="padding:70px 0px 0px 20px; line-height:30px; text-align:inherit; background-color:#84B0CA;" height="100%" valign="top" bgcolor="#84B0CA" role="module-content"><div><div style="font-family: inherit; text-align: left"><span style="font-family: verdana, geneva, sans-serif; color: #ffffff; font-size: 28px"><strong>Our Personal Service</strong></span></div><div></div></div></td>
      </tr>
    </tbody>
  </table><table class="module" role="module" data-type="divider" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="4e843d28-98a5-4618-b25f-a6da881cee6b.1">
    <tbody>
      <tr>
        <td style="padding:10px 140px 20px 20px;" role="module-content" height="100%" valign="top" bgcolor="#84B0CA">
          <table border="0" cellpadding="0" cellspacing="0" align="center" width="100%" height="1px" style="line-height:1px; font-size:1px;">
            <tbody>
              <tr>
                <td style="padding:0px 0px 1px 0px;" bgcolor="#0A3752"></td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
    </tbody>
  </table><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="dJWDTG9nTrW3VZvPPGjtw8.1.1" data-mc-module-version="2019-10-22">
    <tbody>
      <tr>
        <td style="padding:0px 40px 40px 20px; line-height:24px; text-align:inherit; background-color:84B0CA;" height="100%" valign="top" bgcolor="84B0CA" role="module-content"><div><div style="font-family: inherit; text-align: inherit">Expect next-level customer service. We take pride in helping you every step of the way. From figuring out your wants and needs to securing a place on the market, we'll be there to walk you through the entire home-buying process.</div><div></div></div></td>
      </tr>
    </tbody>
  </table></td>
        </tr>
      </tbody>
    </table><table width="266" style="width:266px; border-spacing:0; border-collapse:collapse; margin:0px 0px 0px 0px;" cellpadding="0" cellspacing="0" align="left" border="0" bgcolor="" class="column column-1">
      <tbody>
        <tr>
          <td style="padding:0px;margin:0px;border-spacing:0;"><table class="wrapper" role="module" data-type="image" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="gtVHL9sQjvHtVSuU3huNMR.2">
    <tbody>
      <tr>
        <td style="font-size:6px; line-height:10px; padding:0px 0px 0px 0px;" valign="top" align="center">
          <img class="max-width" border="0" style="display:block; color:#000000; text-decoration:none; font-family:Helvetica, arial, sans-serif; font-size:16px; max-width:100% !important; width:100%; height:auto !important;" width="266" alt="" data-proportionally-constrained="true" data-responsive="true" src="http://cdn.mcauto-images-production.sendgrid.net/c31721ac5f4f8b45/79893087-fc6b-4d4e-97da-c515788b4c63/2208x1469.jpg">
        </td>
      </tr>
    </tbody>
  </table><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="dJWDTG9nTrW3VZvPPGjtw8.3" data-mc-module-version="2019-10-22">
    <tbody>
      <tr>
        <td style="padding:30px 0px 0px 20px; line-height:22px; text-align:inherit; background-color:#0A3752;" height="100%" valign="top" bgcolor="#0A3752" role="module-content"><div><div style="font-family: inherit; text-align: left"><span style="font-family: verdana, geneva, sans-serif; color: #ffffff; font-size: 20px"><strong>1-to-1 meeting</strong></span></div><div></div></div></td>
      </tr>
    </tbody>
  </table><table class="module" role="module" data-type="divider" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="4e843d28-98a5-4618-b25f-a6da881cee6b.1.1">
    <tbody>
      <tr>
        <td style="padding:10px 140px 10px 20px;" role="module-content" height="100%" valign="top" bgcolor="#0A3752">
          <table border="0" cellpadding="0" cellspacing="0" align="center" width="100%" height="1px" style="line-height:1px; font-size:1px;">
            <tbody>
              <tr>
                <td style="padding:0px 0px 1px 0px;" bgcolor="#84B0CA"></td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
    </tbody>
  </table><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="dJWDTG9nTrW3VZvPPGjtw8.2.1.1" data-mc-module-version="2019-10-22">
    <tbody>
      <tr>
        <td style="padding:0px 40px 20px 20px; line-height:18px; text-align:inherit; background-color:#0A3752;" height="100%" valign="top" bgcolor="#0A3752" role="module-content"><div><div style="font-family: inherit; text-align: left"><span style="font-family: verdana, geneva, sans-serif; color: #84b0ca; font-size: 14px">Book an online or onsite appointment with our representative to talk about your dream home anytime, anywhere!</span></div><div></div></div></td>
      </tr>
    </tbody>
  </table><table border="0" cellpadding="0" cellspacing="0" class="module" data-role="module-button" data-type="button" role="module" style="table-layout:fixed;" width="100%" data-muid="75110746-0ccb-4dad-88fc-b77513e11274.1">
      <tbody>
        <tr>
          <td align="left" bgcolor="#0A3752" class="outer-td" style="padding:0px 0px 25px 20px; background-color:#0A3752;">
            <table border="0" cellpadding="0" cellspacing="0" class="wrapper-mobile" style="text-align:center;">
              <tbody>
                <tr>
                <td align="center" bgcolor="#ffffff" class="inner-td" style="border-radius:6px; font-size:16px; text-align:left; background-color:inherit;">
                  <a href="" style="background-color:#ffffff; border:0px solid #7BA1B7; border-color:#7BA1B7; border-radius:0px; border-width:0px; color:#0A3752; display:inline-block; font-size:14px; font-weight:normal; letter-spacing:0px; line-height:normal; padding:12px 18px 12px 18px; text-align:center; text-decoration:none; border-style:solid; font-family:verdana,geneva,sans-serif;" target="_blank">Book now</a>
                </td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
      </tbody>
    </table><table class="module" role="module" data-type="spacer" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="d7f076aa-d5c4-46bd-950b-24471949dd27.1.1">
    <tbody>
      <tr>
        <td style="padding:0px 0px 30px 0px;" role="module-content" bgcolor="#0A3752">
        </td>
      </tr>
    </tbody>
  </table></td>
        </tr>
      </tbody>
    </table><table width="266" style="width:266px; border-spacing:0; border-collapse:collapse; margin:0px 0px 0px 0px;" cellpadding="0" cellspacing="0" align="left" border="0" bgcolor="" class="column column-2">
      <tbody>
        <tr>
          <td style="padding:0px;margin:0px;border-spacing:0;"><table class="wrapper" role="module" data-type="image" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="gtVHL9sQjvHtVSuU3huNMR.1">
    <tbody>
      <tr>
        <td style="font-size:6px; line-height:10px; padding:40px 30px 0px 30px;" valign="top" align="right">
          <img class="max-width" border="0" style="display:block; color:#000000; text-decoration:none; font-family:Helvetica, arial, sans-serif; font-size:16px; max-width:100% !important; width:100%; height:auto !important;" width="266" alt="" data-proportionally-constrained="true" data-responsive="true" src="http://cdn.mcauto-images-production.sendgrid.net/c31721ac5f4f8b45/e4b9d4ad-7ce8-4f2d-9472-0ad433d0ecd1/3283x2189.jpg">
        </td>
      </tr>
    </tbody>
  </table><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="dJWDTG9nTrW3VZvPPGjtw8.1" data-mc-module-version="2019-10-22">
    <tbody>
      <tr>
        <td style="padding:30px 0px 0px 20px; line-height:22px; text-align:inherit; background-color:#84B0CA;" height="100%" valign="top" bgcolor="#84B0CA" role="module-content"><div><div style="font-family: inherit; text-align: left"><span style="font-family: verdana, geneva, sans-serif; color: #ffffff; font-size: 20px"><strong>Estimate your property</strong></span></div><div></div></div></td>
      </tr>
    </tbody>
  </table><table class="module" role="module" data-type="divider" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="4e843d28-98a5-4618-b25f-a6da881cee6b">
    <tbody>
      <tr>
        <td style="padding:10px 140px 10px 20px;" role="module-content" height="100%" valign="top" bgcolor="#84B0CA">
          <table border="0" cellpadding="0" cellspacing="0" align="center" width="100%" height="1px" style="line-height:1px; font-size:1px;">
            <tbody>
              <tr>
                <td style="padding:0px 0px 1px 0px;" bgcolor="#0A3752"></td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
    </tbody>
  </table><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="dJWDTG9nTrW3VZvPPGjtw8.1.1.1" data-mc-module-version="2019-10-22">
    <tbody>
      <tr>
        <td style="padding:0px 40px 20px 20px; line-height:18px; text-align:inherit; background-color:84B0CA;" height="100%" valign="top" bgcolor="84B0CA" role="module-content"><div><div style="font-family: inherit; text-align: left"><span style="font-family: verdana, geneva, sans-serif; color: #0a3752; font-size: 14px">Wonder about the current value for your house? Come to us and we can figure it out for you!</span></div><div></div></div></td>
      </tr>
    </tbody>
  </table><table border="0" cellpadding="0" cellspacing="0" class="module" data-role="module-button" data-type="button" role="module" style="table-layout:fixed;" width="100%" data-muid="fe558c66-0e7c-4f19-8aa0-1c36da292107">
      <tbody>
        <tr>
          <td align="left" bgcolor="84B0CA" class="outer-td" style="padding:0px 0px 25px 20px; background-color:84B0CA;">
            <table border="0" cellpadding="0" cellspacing="0" class="wrapper-mobile" style="text-align:center;">
              <tbody>
                <tr>
                <td align="center" bgcolor="#ffffff" class="inner-td" style="border-radius:6px; font-size:16px; text-align:left; background-color:inherit;">
                  <a href="" style="background-color:#ffffff; border:0px solid #7BA1B7; border-color:#7BA1B7; border-radius:0px; border-width:0px; color:#0A3752; display:inline-block; font-size:14px; font-weight:normal; letter-spacing:0px; line-height:normal; padding:12px 18px 12px 18px; text-align:center; text-decoration:none; border-style:solid;" target="_blank">Find out now</a>
                </td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
      </tbody>
    </table><table class="module" role="module" data-type="spacer" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="d7f076aa-d5c4-46bd-950b-24471949dd27.1">
    <tbody>
      <tr>
        <td style="padding:0px 0px 20px 0px;" role="module-content" bgcolor="">
        </td>
      </tr>
    </tbody>
  </table></td>
        </tr>
      </tbody>
    </table></td>
      </tr>
    </tbody>
  </table><table border="0" cellpadding="0" cellspacing="0" align="center" width="100%" role="module" data-type="columns" style="padding:60px 20px 0px 20px;" bgcolor="" data-distribution="1,3">
    <tbody>
      <tr role="module-content">
        <td height="100%" valign="top"><table width="190" style="width:190px; border-spacing:0; border-collapse:collapse; margin:0px 0px 0px 0px;" cellpadding="0" cellspacing="0" align="left" border="0" bgcolor="" class="column column-0">
      <tbody>
        <tr>
          <td style="padding:0px;margin:0px;border-spacing:0;"><table class="wrapper" role="module" data-type="image" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="c5b00db4-3a79-41fc-b0b1-d30a12bd9260">
    <tbody>
      <tr>
        <td style="font-size:6px; line-height:10px; padding:0px 0px 40px 0px;" valign="top" align="left">
          <img class="max-width" border="0" style="display:block; color:#000000; text-decoration:none; font-family:Helvetica, arial, sans-serif; font-size:16px; max-width:60% !important; width:60%; height:auto !important;" width="114" alt="" data-proportionally-constrained="true" data-responsive="true" src="http://cdn.mcauto-images-production.sendgrid.net/c31721ac5f4f8b45/3f3180b7-e052-41ee-816e-c0201a80fda5/988x189.png">
        </td>
      </tr>
    </tbody>
  </table></td>
        </tr>
      </tbody>
    </table><table width="570" style="width:570px; border-spacing:0; border-collapse:collapse; margin:0px 0px 0px 0px;" cellpadding="0" cellspacing="0" align="left" border="0" bgcolor="" class="column column-1">
      <tbody>
        <tr>
          <td style="padding:0px;margin:0px;border-spacing:0;"><table class="module" role="module" data-type="social" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="3633ff68-f40f-48a8-95bb-60c2758625f3">
    <tbody>
      <tr>
        <td valign="top" style="padding:0px 0px 0px 0px; font-size:6px; line-height:10px;" align="center">
          <table align="center" style="-webkit-margin-start:auto;-webkit-margin-end:auto;">
            <tbody><tr align="center"><td style="padding: 0px 5px;" class="social-icon-column">
      <a role="social-icon-link" href="https://www.facebook.com/sendgrid/" target="_blank" alt="Facebook" title="Facebook" style="display:inline-block; background-color:#0A3752; height:21px; width:21px;">
        <img role="social-icon" alt="Facebook" title="Facebook" src="https://mc.sendgrid.com/assets/social/white/facebook.png" style="height:21px; width:21px;" height="21" width="21">
      </a>
    </td><td style="padding: 0px 5px;" class="social-icon-column">
      <a role="social-icon-link" href="https://twitter.com/sendgrid" target="_blank" alt="Twitter" title="Twitter" style="display:inline-block; background-color:#0A3752; height:21px; width:21px;">
        <img role="social-icon" alt="Twitter" title="Twitter" src="https://mc.sendgrid.com/assets/social/white/twitter.png" style="height:21px; width:21px;" height="21" width="21">
      </a>
    </td><td style="padding: 0px 5px;" class="social-icon-column">
      <a role="social-icon-link" href="https://www.instagram.com/sendgrid/" target="_blank" alt="Instagram" title="Instagram" style="display:inline-block; background-color:#0A3752; height:21px; width:21px;">
        <img role="social-icon" alt="Instagram" title="Instagram" src="https://mc.sendgrid.com/assets/social/white/instagram.png" style="height:21px; width:21px;" height="21" width="21">
      </a>
    </td><td style="padding: 0px 5px;" class="social-icon-column">
      <a role="social-icon-link" href="https://www.pinterest.com/sendgrid/" target="_blank" alt="Pinterest" title="Pinterest" style="display:inline-block; background-color:#0A3752; height:21px; width:21px;">
        <img role="social-icon" alt="Pinterest" title="Pinterest" src="https://mc.sendgrid.com/assets/social/white/pinterest.png" style="height:21px; width:21px;" height="21" width="21">
      </a>
    </td><td style="padding: 0px 5px;" class="social-icon-column">
      <a role="social-icon-link" href="https://www.linkedin.com/company/sendgrid/" target="_blank" alt="LinkedIn" title="LinkedIn" style="display:inline-block; background-color:#0A3752; height:21px; width:21px;">
        <img role="social-icon" alt="LinkedIn" title="LinkedIn" src="https://mc.sendgrid.com/assets/social/white/linkedin.png" style="height:21px; width:21px;" height="21" width="21">
      </a>
    </td></tr></tbody>
          </table>
        </td>
      </tr>
    </tbody>
  </table><div data-role="module-unsubscribe" class="module" role="module" data-type="unsubscribe" style="color:#0A3752; font-size:12px; line-height:20px; padding:20px 0px 16px 0px; text-align:center;" data-muid="4e838cf3-9892-4a6d-94d6-170e474d21e5"><div class="Unsubscribe--addressLine"><p class="Unsubscribe--senderName" style="font-family:verdana,geneva,sans-serif; font-size:12px; line-height:20px;">{{Sender_Name}}</p><p style="font-family:verdana,geneva,sans-serif; font-size:12px; line-height:20px;"><span class="Unsubscribe--senderAddress">{{Sender_Address}}</span>, <span class="Unsubscribe--senderCity">{{Sender_City}}</span>, <span class="Unsubscribe--senderState">{{Sender_State}}</span> <span class="Unsubscribe--senderZip">{{Sender_Zip}}</span></p></div><p style="font-family:verdana,geneva,sans-serif; font-size:12px; line-height:20px;"><a class="Unsubscribe--unsubscribeLink" href="{{{unsubscribe}}}" target="_blank" style="color:#84B0CA;">Unsubscribe</a> - <a href="{{{unsubscribe_preferences}}}" target="_blank" class="Unsubscribe--unsubscribePreferences" style="color:#84B0CA;">Unsubscribe Preferences</a></p></div></td>
        </tr>
      </tbody>
    </table></td>
      </tr>
    </tbody>
  </table><table border="0" cellpadding="0" cellspacing="0" class="module" data-role="module-button" data-type="button" role="module" style="table-layout:fixed;" width="100%" data-muid="9da66b13-896d-4256-b4ba-d1758a6ef5b8">
      <tbody>
        <tr>
          <td align="center" bgcolor="" class="outer-td" style="padding:20px 0px 20px 0px;">
            <table border="0" cellpadding="0" cellspacing="0" class="wrapper-mobile" style="text-align:center;">
              <tbody>
                <tr>
                <td align="center" bgcolor="#F5F8FD" class="inner-td" style="border-radius:6px; font-size:16px; text-align:center; background-color:inherit;">
                  <a href="https://sendgrid.com/" style="background-color:#F5F8FD; border:1px solid #F5F8FD; border-color:#F5F8FD; border-radius:25px; border-width:1px; color:#A8B9D5; display:inline-block; font-size:10px; font-weight:normal; letter-spacing:0px; line-height:normal; padding:5px 18px 5px 18px; text-align:center; text-decoration:none; border-style:solid; font-family:helvetica,sans-serif;" target="_blank">♥ POWERED BY TWILIO SENDGRID</a>
                </td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
      </tbody>
    </table></td>
                                      </tr>
                                    </table>
                                    <!--[if mso]>
                                  </td>
                                </tr>
                              </table>
                            </center>
                            <![endif]-->
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
          </table>
        </div>
      </center>
    </body>
  </html>
'''
        # html_content='<strong>and easy to do anywhere, even with Python</strong>'
    )

    try:
        sg = SendGridAPIClient('')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    send_email()
